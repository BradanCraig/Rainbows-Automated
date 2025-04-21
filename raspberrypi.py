import os
import subprocess


#This may be quite dangerous to OS Injection, before deployment please check security risks
#The command is safe to run as there is no malicious intent but direct injection like this can be a HUGE cyber threat if not properly sanitized

#this stuff is also hard coded in. For deployment a database will have to be implimented as well as a set up wizzard for all of the raspberry pi stuff.

def run_script(script_name="/home/lizawhite/Desktop/SetupCode.py"):
    print("ran")
    result_message = subprocess.run(f"ssh lizawhite@10.4.119.62 python3 {script_name}")
    print(result_message)
    if result_message.returncode == 0:
        local_path = "C:/HowelLab/Rainbows/Automated_Rainbows/Rainbows-Automated/images"
        scp_command = f'scp lizawhite@10.4.119.62:/home/lizawhite/image.jpg "{local_path}"'
        pulling_img_message = subprocess.run(scp_command, shell=True)
        print(pulling_img_message)
    else:
        raise Exception("Command failed executing script")
    return 0

    #This now runs the script on the Raspberry Pi, need the camera re connected and to re configure the script to take input parameters
    #also need to grab the file system afterward to analyze
    #need to make it so that the server starts on boot. Go into nano files 
