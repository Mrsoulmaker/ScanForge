## Description:-

This Python Port Scanner Tool is a lightweight utility designed for network administrators and security professionals to scan target hosts for open ports and identify associated services. With the ability to perform basic vulnerability checks for specific services like HTTP, FTP, and RDP, the tool provides valuable insights into the security posture of network assets. Utilizing threading for efficient scanning and a user-friendly command-line interface, it offers a simple yet effective solution for assessing network security.

## Key Feature:-

- Port Scanning:
The script allows users to input one or more target hosts separated by commas.
Users can specify a port range (e.g., 1-1024) or a single port to scan.
It uses threading to scan multiple hosts simultaneously, improving efficiency.
- Vulnerability Checks:
For specific services running on open ports (HTTP, FTP, SMB, RDP, etc.), the script performs vulnerability checks.
Currently, the vulnerability check is implemented for the HTTP service (port 80) using the requests library.
Additional vulnerability checks can be added as needed for other services by extending the check_vulnerabilities() function.
- Multithreading:
The script utilizes threading to scan multiple ports for each host concurrently, improving scanning speed.
- User Interaction:
The script prompts users to input target hosts and port ranges interactively.
It handles user input errors gracefully, such as invalid port ranges.
- Error Handling:
The script includes error handling for potential socket errors that may occur during port scanning.
- Output Formatting:
The script provides clear and informative output, indicating the status of each port and any identified services or vulnerabilities.

## Pre-Requirements:- 

- Python Environment: Ensure that Python is installed on the system where the code will be executed. The code is written in Python, so a compatible Python interpreter is required.
- Requests Library: The code utilizes the requests library for performing HTTP vulnerability checks. Therefore, the requests library must be installed. This can be done using the following command:
  
           pip install requests

-Network Connectivity: The code performs port scanning and vulnerability checks over the network. Ensure that the system running the code has network connectivity to the target hosts.
-Target Hosts and Ports: Users need to input the target hosts (IP addresses or domain names) separated by commas and the port range or single port to scan. Ensure that the target hosts are reachable from the system where the code is executed, and the specified ports are accessible for scanning.

## Usage:- 

Users can clone the repository and execute the Python script locally on their systems. The tool prompts users to input target hosts and port ranges interactively, making it accessible to both beginners and experienced users. 

- Change the Directory to ScanForge

          cd ScanForge

- Use this command to run the tool
    
        python3 ScanForge 

## Output

 ![image](https://github.com/Mrsoulmaker/ScanForge/assets/91201990/0882e253-6356-42af-b81c-0d60fb44f79d)


## Contributions:-

Contributions to the tool, such as feature enhancements, bug fixes, and documentation improvements, are welcome. Users can submit pull requests or raise issues to contribute to the ongoing development and improvement of the tool.

## License:
The tool is distributed under an open-source license (e.g., GNU License), allowing users to modify, distribute, and use the code for both personal and commercial purposes. The license details are included in the repository for clarity and transparency.

## Acknowledgments:-

The tool may include acknowledgments for libraries, resources, or individuals whose contributions have been instrumental in its development. These acknowledgments highlight the collaborative nature of open-source software development and recognize the valuable contributions of the community.
