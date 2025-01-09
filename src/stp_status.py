"""
================================================================
File_Name: stp_status.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: This script is part of the STP project, which aims
to document the STP status.
License: GPLv3
Dependencies: telnetlib
================================================================
""" 
import telnetlib
import time
def stp_status(HOST, password, enable_password):
    try:
        # Establish the connection
        tn = telnetlib.Telnet(HOST)  
        tn.write(password.encode('ascii') + b"\n")
        # Change the mode
        tn.write(b"enable\n")
        tn.write(enable_password.encode('ascii') + b"\n")
        # Run the command
        tn.write(b"show spanning-tree\n")
        # Caputure the output
        stp_output = tn.read_very_eager().decode('ascii')
        # Exit
        tn.write(b"exit\n")

        return stp_output

    except Exception as e:
        return f"Error occurred: {str(e)}"
# Check whether the program is called from main or locally
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")



    
        
      
  
        
        
        
