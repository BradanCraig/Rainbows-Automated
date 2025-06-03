from flask import Flask, render_template, request, session, redirect, flash, url_for, jsonify
from functools import wraps
from raspberrypi import *
from database_funcs import *
import requests
import base64
from helpers import *
import time
import threading
import secrets
from bson.objectid import ObjectId

app=Flask(__name__)

#Globals
thread=None
stop_pictures = threading.Event()

#add @login_required to any path that needs to have a session
#this ensures that the username is in the session and can be accessed
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to be logged in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    client_ip = request.remote_addr
    print(client_ip)
    return render_template("home.html")



@app.route("/livestream")
@login_required
def livestream():
    return "Need to get the IP from the Raspberry Pi"



@app.route("/run")
@login_required
def run():
    return render_template("run.html", run=run_script)



@app.route('/send_dur_and_freq', methods=['POST'])
def sending_data(stoping, duration, frequency):

    url = 'http://10.4.119.62:5000/get_images'
    data = {'duration': duration, 'frequency': frequency}
    headers = {'Content-Type': 'application/json'}
    
    if duration != None:
        try:
            number_of_images = (duration*frequency)
            for i in range(number_of_images+1):

                if stoping.is_set():
                    return "Stopped Early"
                
                #Turn On LED

                response = requests.post(url, json=data, headers=headers)
                image = decode_image(encoded_img=response.json()['image'])
                image.save(f"images/image_{i}.png")
                
                #turn off LED

                if i != number_of_images:
                    time.sleep(((1/frequency)*60)-.1)#needs to sleep for that amount of time in the code for LED to turn on
            
            print("done")
            return "Received Message"

        except requests.exceptions.RequestException as e:
            print(e)
            return f"Error sending data: {e}", 500

    else:
        while True:
            print(duration, frequency)
            if stoping.is_set():
                    return "Stopped Early"
                
                #Turn On LED

            response = requests.post(url, json=data, headers=headers)
            image = decode_image(encoded_img=response.json()['image'])
            image.save(f"images/image_{i}.png")
                
                #turn off LED

            if i != number_of_images:
                time.sleep(((1/frequency)*360)-.1)


@app.route("/stop")
def stop():
    global stop_pictures
    stop_pictures.set()
    return "Stopped"



@app.route("/start", methods=["POST"])
def start():
        
    data = request.get_json()
    duration = data.get("duration")
    frequency = data.get("frequency")

    global thread, stop_pictures
    if thread is None or not thread.is_alive():
        stop_pictures.clear()
        thread = threading.Thread(target=sending_data, args=(stop_pictures, duration, frequency))
        thread.start()
        
    return "started"



@app.route("/setup")
@login_required
def setup():
    return render_template("setup.html")



@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = authorize(username=username, password=password)
    if user != None:
        print("hit")
        session["user_id"] = str(user["_id"])
        return jsonify({'success': True, 'redirect': url_for('home')})
    else:
        flash("Incorrect Password or Username", "error")
        return jsonify({'success': False, 'message': 'Invalid Credentials'})



@app.route("/logout")
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route("/get_systems", methods=["GET"])
def get_systems():
    user=get_user(ObjectId(session['user_id']))
    return jsonify({'systems': user['systems']})



if __name__ =="__main__":
    app.secret_key = '1234', #secrets.token_urlsafe(32)
    app.run(debug=True, port=5000)




