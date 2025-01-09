"""
================================================================
File_Name: main.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: This is the main.py script, which aims to call
functions from other modules
License: GPLv3
Dependencies: telnetlib
================================================================
"""
from mypaths import telnet_pass as telnt
import src.stp_status as staus
import src.stp_mitigate as mitg

def main():
    host = telnt["HOST"]
    password = telnt["password"]
    enable_password = telnt["enable_password"]
    port = telnt["port"]

    # Call the function
    stp_status_output = staus.stp_status(host, password, enable_password)
    print(stp_status_output)
    stp_mitigate_output = mitg.stp_mitigate(host, password, enable_password, port)
    print(stp_mitigate_output)

if __name__ == "__main__":
    main()
