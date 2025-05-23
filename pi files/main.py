#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, jsonify
from camera import VideoCamera
import os

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture', methods=['POST'])
def take_picture():
    pi_camera.take_picture()
    return "None"

@app.route('/get_images', methods=['POST'])
def get_images():
    try:
        data=request.get_json()
        print("received data", data)
    
        image = pi_camera.capture_image()
        
        
        files = {'image': image}
        return jsonify(files), 200 
    
    except Exeption as e:
        print(e)
        return jsonify({"message": str(e)}), 200    

if __name__ == '__main__':

    app.run(host='10.4.119.62', debug=False, port=8000)
