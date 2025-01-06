"""
================================================================
File_Name: stp.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: This script is part of the STP project, which aims
to document the STP status.
License: GPLv3
Dependencies: paramiko, logging, requests
================================================================
"""
import paramiko
import settings.ssh_pass as sh

# Create an SSH client
ssh = paramiko.SSHClient()

# Function document stp status
def stp_staus(vlan_ip, sw_username, sw_pass):
    
    # Load SSH host keys. 
    ssh.load_system_host_keys()
    # Add SSH host key when missing:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
    # Connecto to the switch 
     ssh.connect(vlan_ip,username=sw_username,password=sw_pass)
      # Execute STP status command
     command = "show spanning-tree"
     ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
     stp_output = ssh_stdout.readlines()
       # Close the ssh connection
     ssh.close()
     return stp_output
    except Exception as error_message:
     print("Connection error")
     print (error_message)
      

# Check the script is called from main or other mdodul
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Variable declaration    
    ip= sh.SSH["ip_address"]
    username=sh.SSH["username"]
    password = password=sh.SSH["password"]  
    # Call function      
    stp_staus(ip, username, password,)
else:
    print(f"This module is called {__name__} and is being called by another script")
    
        
      
  
        
        
        
