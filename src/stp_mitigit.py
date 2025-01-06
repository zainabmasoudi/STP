
"""
================================================================
File_Name: stp.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: This script is part of the STP project, which aims
to mitigate STP loops.
License: GPLv3
Dependencies: paramiko
================================================================
"""
import paramiko 
import settings.ssh_pass as sh

# Create an SSH client
ssh = paramiko.SSHClient()

# Function mitigates the STP loop
def stp_mitigate(vlan_ip, sw_username, sw_pass, port):
    
    # Load SSH host keys. 
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the switch
        ssh.connect(vlan_ip, username=sw_pass, password=sw_pass, port=port )
        # Shutdown the port 
        config_command = f'interface {port}\nshutdown'
        stdin, stdout, stderr = ssh.exec_command(config_command)
        output = stdout.read().decode()
        print(output)
        # Close the ssh connection
        ssh.close()
    except  Exception as error_message:
        print("Connection error")
        print (error_message)
     
# Check the script is called from main or other mdodul
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Variable declaration    
    IP = sh.SSH["ip_address"]
    username=sh.SSH["username"]
    password = sh.SSH["password"]  
    port = sh.SSH["port"]      
    # Calling the function
    stp_mitigate(IP, username, password, port)    
else:
    print(f"This module is called {__name__} and is being called by another script")
    
 


