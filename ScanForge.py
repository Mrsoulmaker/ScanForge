import socket
import threading
import requests  # For HTTP vulnerability checks (requires installation)

# Dictionary mapping port numbers to their associated service names
SERVICE_PORTS = {
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    445: "SMB",
    3389: "RDP",
    4899: "Radmin",
    5800: "Radmin",
    5900: "Radmin"
}

# Function to check for vulnerabilities associated with specific services
def check_vulnerabilities(host, port):
    service_name = SERVICE_PORTS.get(port, None)
    if service_name:
        if port == 80:  # HTTP vulnerability check
            url = f"http://{host}:{port}/"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"Vulnerability check: {url} is accessible.")
                    # Add more vulnerability checks as needed for other services
                else:
                    print(f"Vulnerability check: {url} returned status code {response.status_code}.")
            except requests.RequestException as e:
                print(f"Vulnerability check: Error occurred while checking {url}: {e}")
        # Add more vulnerability checks for other services
    else:
        print(f"No vulnerability checks available for port {port}.")

# Function to scan a single port
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Adjust timeout as needed
            result = sock.connect_ex((host, port))
            if result == 0:
                service_name = SERVICE_PORTS.get(port, None)
                if service_name:
                    print(f"Port {port} on {host} is open, Service: {service_name}")

                    # Additional checks for specific services
                    if port == 80:
                        print(f"HTTP service running at http://{host}:{port}")
                else:
                    print(f"Port {port} on {host} is open")
                    check_vulnerabilities(host, port)
            else:
                print(f"Port {port} on {host} is closed")
    except socket.error:
        print("Error occurred while scanning port")

# Function to scan ports for a single host
def scan_host(host, ports):
    print(f"Scanning host {host}...")
    for port in ports:
        scan_port(host, port)

# Function to scan ports for multiple hosts
def scan_hosts(hosts, ports):
    print(f"Scanning {len(hosts)} hosts for {len(ports)} ports...")
    threads = []
    for host in hosts:
        thread = threading.Thread(target=scan_host, args=(host, ports))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Main function
def main():
    target_hosts = input("Enter target host(s) separated by comma (e.g., 127.0.0.1,192.168.0.1): ").split(",")
    target_ports = input("Enter port range (e.g., 1-1024) or single port (e.g., 80): ")
    if "-" in target_ports:
        start_port, end_port = map(int, target_ports.split("-"))
        target_ports = range(start_port, end_port + 1)
    else:
        target_ports = [int(target_ports)]
    scan_hosts(target_hosts, target_ports)

if __name__ == "__main__":
    main()
