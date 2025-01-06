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
Dependencies: paramika
================================================================
"""
import source.stp_doc as STP_Doc
import source.stp_mitigit as STP_Mit
from mypaths import ssh_pass as ssh_settings

Check_STP = STP_Doc.stp_staus(ssh_settings.SSH["ip_address"], ssh_settings.SSH["username"], ssh_settings.SSH["password"])
STP_Mitigate = STP_Mit.stp_mitigate(ssh_settings.SSH["ip_address"], ssh_settings.SSH["username"], ssh_settings.SSH["password"], ssh_settings.SSH["port"])
