"""
================================================================
File_Name: mypath.py
Author: Zainab Masoudi
Contact: zainab.masoudi@yahoo.com
Date: 2024-11-29
Version: 1.0
Description: Path declariation 
License: GPLv3
Dependencies: telnetlib
================================================================
"""

from pathlib import Path
Project_Root = Path(__file__).parent
telnet_pass = str(Project_Root / "STP/settings/telnet_pass.py")
