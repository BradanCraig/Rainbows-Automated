from flask import Flask, render_template, request
from raspberrypi import *
import requests
import base64
from helpers import *
import time


app=Flask(__name__)



@app.route('/')
def home():
    client_ip = request.remote_addr
    print(client_ip)
    return render_template("home.html")



@app.route("/livestream")
def livestream():
    return "Need to get the IP from the Raspberry Pi"



@app.route("/run")
def run():
    return render_template("run.html", run=run_script)



@app.route('/send_dur_and_freq', methods=['POST'])
def sending_data():
    data = request.get_json()
    duration = data.get("duration")
    frequency = data.get("frequency")


    
    url = 'http://10.4.119.62:8000/get_images'
    data = {'duration': duration, 'frequency': frequency}
    headers = {'Content-Type': 'application/json'}

    try:
        number_of_images = (duration*frequency)
        for i in range(number_of_images+1):
            
            response = requests.post(url, json=data, headers=headers)
            image = decode_image(encoded_img=response.json()['image'])
            image.save(f"images/image_{i}.png")
            
            if i != number_of_images:
                time.sleep((1/frequency)*60)
        
        print("done")
        return "Received Message"

    except requests.exceptions.RequestException as e:
        print(e)
        return f"Error sending data: {e}", 500


@app.route("/setup")
def setup():
    return render_template("setup.html")

if __name__ =="__main__":
    app.run(debug=True, port=5000)



