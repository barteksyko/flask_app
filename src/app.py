from tkinter.tix import Tree
from tkgpio import TkCircuit

configuration = {
    "width": 925,
    "height": 600,
    "toggles": [
        {
            "x": 100,
            "y": 40,
            "name": " TO1 Start/Stop",
            "pin": 15,
        },
        {
            "x": 410,
            "y": 40,
            "name": " TO2 Start/Stop",
            "pin": 13,
        },
        {
            "x": 720,
            "y": 40,
            "name": " ODZ Start/Stop",
            "pin": 11,
        },
    ],
    "leds": [
        {"x": 140, "y": 100, "name": "TO1", "pin": 16},
        {"x": 450, "y": 100, "name": "TO2", "pin": 19},
        {"x": 760, "y": 100, "name": "ODZ", "pin": 21},
    ],
    "adc": {
        "mcp_chip": 3008,
        "potenciometers": [
            {"x": 80, "y": 170, "name": "Speed Potentiometer TO1", "channel": 0},
            {"x": 385, "y": 170, "name": "Speed Potentiometer TO2", "channel": 2},
            {"x": 695, "y": 170, "name": "Speed Potentiometer ODZ", "channel": 6},
        ],
    },
    "motors": [
        {
            "x": 120,
            "y": 230,
            "name": "Motor TO1",
            "forward_pin": 22,
            "backward_pin": 23,
        },
        {
            "x": 430,
            "y": 230,
            "name": "Motor TO2",
            "forward_pin": 26,
            "backward_pin": 23,
        },
        {
            "x": 740,
            "y": 230,
            "name": "Motor ODZ",
            "forward_pin": 20,
            "backward_pin": 23,
        },
    ],
    "lcds": [
        {
            "x": 180,
            "y": 420,
            "name": "LCD",
            "pins": [2, 3, 4, 5, 6, 7],
            "columns": 16,
            "lines": 2,
        },
        {
            "x": 500,
            "y": 420,
            "name": "LCD",
            "pins": [8, 25, 18, 14, 17, 27],
            "columns": 16,
            "lines": 2,
        },
    ],
    "labels": [
        {
            "x": 15,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
        {
            "x": 320,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
        {
            "x": 625,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
    ],
}

circuit = TkCircuit(configuration)


@circuit.run
def main():
    from gpiozero import LED, Button, MCP3008, Motor
    from time import sleep
    from Adafruit_CharLCD import Adafruit_CharLCD
    from flask import Flask, render_template, request
    import sys
    from tkinter.tix import Tree

    work_led_TO1 = LED(16)
    work_led_TO2 = LED(19)
    work_led_ODZ = LED(21)
    potenciometer1_TO1 = MCP3008(0)
    potenciometer2_TO2 = MCP3008(2)
    potenciometer3_ODZ = MCP3008(6)
    motor_TO1 = Motor(22, 23)
    motor_TO2 = Motor(26, 24)
    motor_ODZ = Motor(20, 12)
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    lcd2 = Adafruit_CharLCD(8, 25, 18, 14, 17, 27, 16, 2)
    switch_TO1 = Button(15)
    swtich_TO2 = Button(13)
    switch_ODZ = Button(11)

    app = Flask(__name__)

    @app.route("/", methods=("GET", "POST"))
    @app.route("/index", methods=["POST", "GET"])
    def index():

        if request.method == "POST":

            current = request.form["current"]
            current2 = request.form["current2"]
            current3 = request.form["current3"]
            return render_template("index.html")

        return render_template("index.html")

    @app.route("/slider_update", methods=["POST", "GET"])
    def slider():

        received_data = request.data
        received_data = float(received_data) / 50
        motor_TO1.forward(received_data)
        motor_TO1.value = received_data

        return str(received_data)

    @app.route("/slider_update2", methods=["POST", "GET"])
    def slider2():

        received_data = request.data
        received_data = float(received_data) / 50
        motor_TO2.forward(received_data)
        motor_TO2.value = received_data

        return str(received_data)

    @app.route("/slider_update3", methods=["POST", "GET"])
    def slider3():

        received_data = request.data
        received_data = float(received_data) / 50
        motor_ODZ.forward(received_data)
        motor_ODZ.value = received_data

        return str(received_data)

    @app.route("/check_update", methods=["POST", "GET"])
    def check():

        received_data = request.data
        received_data = str(received_data).replace("'", "")[1:]

        if received_data == "false":
            work_led_TO1.off()
            motor_TO1.stop()

        elif received_data == "true":
            work_led_TO1.on()
            motor_TO1.forward()

        return received_data

    @app.route("/check_update2", methods=["POST", "GET"])
    def check2():
        received_data = request.data
        received_data = str(received_data).replace("'", "")[1:]

        if received_data == "false":
            work_led_TO2.off()
            motor_TO2.stop()

        elif received_data == "true":
            work_led_TO2.on()
            motor_TO2.forward()

        return received_data

    @app.route("/check_update3", methods=["POST", "GET"])
    def check3():
        received_data = request.data
        received_data = str(received_data).replace("'", "")[1:]

        if received_data == "false":
            work_led_ODZ.off()
            motor_ODZ.stop()

        elif received_data == "true":
            work_led_ODZ.on()
            motor_ODZ.forward()

        return received_data

    while True:
        app.run()

        check()
        slider()
        check2()
        slider2()
        check3()
        slider3()
