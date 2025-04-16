from flask import Flask, render_template
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

@app.route('/<FUNCTION>')
def command(FUNCTION=None):
    exec(FUNCTION.replace("<br>", "\n"))
    return""

def call_command(script_name=None):
    run_script(script_name=script_name)



if __name__ =="__main__":
    app.run(debug=True)



