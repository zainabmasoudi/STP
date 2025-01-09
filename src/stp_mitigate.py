
"""
================================================================
File_Name: stp_mitigate.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: This script is part of the STP project, which aims
to mitigate STP loops.
License: GPLv3
Dependencies: telnetlib
================================================================
"""  
import telnetlib
import time

def stp_mitigate(HOST, password, enable_password, port):
    try:
        # Establish connection
        tn = telnetlib.Telnet(HOST)  

        tn.write(password.encode('ascii') + b"\n")
        # Change mode
        tn.write(b"enable\n")
        tn.write(enable_password.encode('ascii') + b"\n")
        # Globale configuration mode
        tn.write(b"config t\n")
        # Run command
        command = f"interface {port}\nshutdown\n".encode('ascii')
        tn.write(command)
        # Capture output
        stp_output = tn.read_very_eager().decode('ascii')
        # Exit
        tn.write(b"exit\n")

        return stp_output

    except Exception as e:
        return f"Error occurred: {str(e)}"
    
# Check the program is run localy or from main     
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")




 


