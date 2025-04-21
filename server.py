from flask import Flask, render_template, request
from raspberrypi import *






app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/livestream")
def livestream():
    return "Need to get the IP from the Raspberry Pi"

@app.route("/run")
def run():
    return render_template("run.html", run=run_script)

#This takes the run_script post request and calls the run script command in another file
@app.route('/run_script', methods=['POST'])
def run_script_route():
    data = request.get_json()
    duration = data.get("duration")
    frequency = data.get("frequency")
    
    print(f"durration={duration}\nFrequency={frequency}")
    
    run_script(duration=duration, frequency=frequency)


if __name__ =="__main__":
    app.run(debug=True)



