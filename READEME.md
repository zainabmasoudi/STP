# Spanning Tree Protocol (STP) Documentation and Mitigation
## Description 
Spanning Tree Protocol (STP) is a network protocol used to prevent loops in Layer 2 (data link layer) switches, ensuring network redundancy. In this project, we use Python to automate tasks related to STP status documentation and mitigation.
## Aim
The goal of this project is to automate the verification of STP status and apply mitigation strategies to prevent STP loops across network devices (such as Cisco switches) using Python.
## Project Scope
The project includes three main tasks:
1. __Verify the current STP status__ by running `show spanning tree` or `display stp brief` commands.
2. __Document key STP status information__ such as port bridge information and port status.
3. __Apply mitigation strategies__ by disabling extra switch ports to prevent STP loops.
## Method
1. __Configure SSH on the Cisco Switch__ the configuration steps are included in __docs__ directory.
2. __Automate Directory Creation__
   The `directory_automation.bat` script automates the creation of essential project directories: `documentation`, `source`, `settings`, `templates`, and `test`.

3. __Main Python Scripts__
   - `stp_doc.py`: Connects to the switch, retrieves the STP status, and documents the findings.
   - `stp_mitigate.py`: Applies mitigation strategies to disable extra switch ports for network stability.
   - `main.py`: Entry point for executing the project. It invokes the `stp_doc` and `stp_mitigate` functions.

4. **Project Structure**
   - The project uses Python packages for modularity:
   - `settings`: Contains SSH credentials securely stored in `ssh_pass.py`.
   - `templates`: Includes reusable headers (`header.py`) for consistency across modules.
   - `test`: Includes testing results (e.g., Pylint).

5. **Testing**
   - The `test` directory includes the results of a Pylint scan. The code quality is reviewed, and some errors related to variable naming conventions and whitespace usage were noted.

## Project Conclusion 
This project provides a hands-on experience in structuring a Python-based automation tool for network tasks. It covers essential concepts such as SSH connection handling, STP monitoring, and mitigation. Additionally, it demonstrates good coding practices and modular programming in Python.