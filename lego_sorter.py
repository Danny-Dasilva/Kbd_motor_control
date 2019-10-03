
from app import Detect, Classify, Teachable, Empty
from flask import Flask, send_file, Response, render_template
from app.Cam import camera
import keyboard
from time import sleep
import time
from threading import Thread, active_count
import signal
from threading import Thread, Event
from threading import Thread
import sys
import serial
from adafruit_servokit import ServoKit

import keyboard

values = {1 : "a", 2 : "d", 3 : "w", 4: "s"}



def angle_gen(length):
    angle = 360 / length
    return(angle)

app = Flask(__name__)


Image = camera(Teachable.AI())




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(Image.ImageStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def flaskServer():
    app.run(host="0.0.0.0", debug=False)

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

def Robot_code():
    global position

    target = 0
    drop_flag = False
    kit = ServoKit(channels=16)
    start_flag = False
    while True:
        sleep(0.01)
        #result = Image.val
        result = keyboard.read_key()
        for key, value in values.items():
            if(not drop_flag and start_flag):
                if(result == "Board"):
                    pass
                if keyboard.is_pressed(value):
                    mult = angle_gen(len(values))
                    print(key * mult, "is pressed")
                    target = key * mult
                    drop_flag = True
        if result == "p":
            print("You pressed p")
            break
        if(result == "Start"):
            start_flag = True
        if(drop_flag):
                drop_flag = False
                kit.servo[0].angle = 15



if __name__ == "__main__":
    global status
    global position
    global kit

    position = 0
    thread = Thread(target=flaskServer)
    thread.start()
    thread3 = Thread(target=Robot_code)
    thread3.start()
