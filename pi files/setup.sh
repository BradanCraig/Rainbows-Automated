#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip

sudo at pip3 install numpy Picamera2 cv time datetime numpy base64 Flask

#need to write the commands in order to run the server on boot

