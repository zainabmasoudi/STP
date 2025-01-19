# Spanning Tree Protocol (STP) Documentation and Mitigation
## Description 
Spanning Tree Protocol (STP) is a network protocol utilized in Ethernet networks to prevent loops in Layer 2 (data link layer) switches and enhance network redundancy.
In this project, we are going to write a Python code to document the status of STP and mitigate STP loops.

## Aim
The primary goal of this project is to use Python code for automating the network tasks and running the list of commands simultaneously across multiple devices in the network.
## Project Scope
This project covers three main taks:
1. Verifying the current status of STP by running ``` show spanning tree ``` or ``` display stp brief``` command on the switch.
2. Documenting key information about the STP status like port Bridge information and ports. 
3. Apply mitigation strategies to prevent an STP loop in the network.
## Methodology
### Telnet Configuration 
Telnet has been configured in the Cisco switch to provide a remote connection.
### Directory and File Automation
__directory_automation.bat__ script file is written to automate the process of files and directories creation in this project. Runing this script will generate the following folder structure.

1. __docs:__ Stores project related documents.
2. __scripts:__ Contains the batch script to automate the directory creation.
3. __settings:__ Stores switch related information (e.g., username, password and IP).
4. __src:__ Includes the main Python modules to connect with switch.
5. __templates:__ holds on project general header style.
6. __tests:__ Contains the *pylint* test result.
7. __images:__ Contains the screenshot of tested script in gns3 
### Python Modules Overview
1. ``stp_status.py``: Establish an ssh connection to a cisco switch and display the STP status.
2. ``stp_mitigate.py``: Connects to the switches and applies mitigation policy by disabling extra switch port to enhance network stability.
3. ``main.py``: The central script that imports and call functions from __stp_status.py__ and __stp_mitigate.py__ to run the entire process.
### Testing and Quality Assurance
 1. __Pylint:__ The pylint was run to check the quality of the code. Some issues were identified both in the stp_status.py and stp_mitigit.py modules (e.g., non-standard variable names and whitespace errors).
 2. __Unittest:__ The unittest is used to make sure that every piece of our project is working properly.

## Project Conclusion 
By carrying this project out, we gained a fundamental understanding of structuring a Python project from start to end. We learned how different modules and packages interact and how to import functions and variables from one package to another. Additionally, we understood how to use Python code for automating network tasks particularly, running several network commands simultaneously.
