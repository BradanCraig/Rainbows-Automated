import os
import subprocess


#This may be quite dangerous to OS Injection, before deployment please check security risks
#The command is safe to run as there is no malicious intent but direct injection like this can be a HUGE cyber threat if not properly sanitized

#this stuff is also hard coded in. For deployment a database will have to be implimented as well as a set up wizzard for all of the raspberry pi stuff.

def run_script(script_name="/home/lizawhite/Desktop/Code_for_Camera_Capture.py"):
    print("ran")
    result_message = subprocess.run(f"ssh lizawhite@10.4.119.62 python3 {script_name}")
    print(result_message)
    return 0

    #This now runs the script on the Raspberry Pi, need the camera re connected and to re configure the script to take input parameters
    #also need to grab the file system afterward to analyze
    #need to make it so that the server starts on boot. Go into nano files 
