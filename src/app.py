# from tkinter.tix import Tree
from tkgpio import TkCircuit
from configurationsTkCircuit import configuration


circuit = TkCircuit(configuration)


@circuit.run
def flask_app():
    from gpiozero import LED, Button, MCP3008, Motor
    from time import sleep
    from Adafruit_CharLCD import Adafruit_CharLCD
    from flask import Flask, render_template, request

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
        lcd.clear()
        lcd.message("TO1 Hz: %.2f" % (received_data * 50))

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
            work_led_TO2.off()
            motor_TO2.stop()
            work_led_ODZ.off()
            motor_ODZ.stop()

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

    # @app.route("/check_update4", methods=["POST", "GET"])
    # def check4():
    #     received_data = request.data
    #     received_data = str(received_data).replace("'", "")[1:]

    #     # if received_data == "false":
    #     #     work_led_ODZ.off()
    #     #     motor_ODZ.stop()

    #     # elif received_data == "true":
    #     #     work_led_ODZ.on()
    #     #     motor_ODZ.forward()
    #     while True:
    #         if switch_TO1.is_pressed:
    #             work_led_TO1.on()
    #             motor_TO1.forward(potenciometer1_TO1.value)
    #             print(type(potenciometer1_TO1.value), potenciometer1_TO1.value)
    #             lcd.clear()
    #             lcd.message("TO1 Hz: %.2f" % (potenciometer1_TO1.value * 50))
    #             if swtich_TO2.is_pressed:
    #                 work_led_TO2.on()
    #                 motor_TO2.forward(potenciometer2_TO2.value)
    #                 lcd2.clear()
    #                 lcd2.message("TO2: %.2f" % (potenciometer2_TO2.value * 50))
    #                 if switch_ODZ.is_pressed:
    #                     work_led_ODZ.on()
    #                     motor_ODZ.forward(potenciometer3_ODZ.value)
    #                 else:
    #                     work_led_ODZ.off()
    #                     motor_ODZ.stop()
    #             else:
    #                 work_led_TO2.off()
    #                 work_led_ODZ.off()
    #                 motor_TO2.stop()
    #                 motor_ODZ.stop()
    #                 lcd2.clear()
    #                 lcd2.message("TO2 Hz: %.2f" % (0))
    #         else:
    #             work_led_TO1.off()
    #             work_led_TO2.off()
    #             work_led_ODZ.off()
    #             motor_TO1.stop()
    #             motor_TO2.stop()
    #             motor_ODZ.stop()
    #             lcd.clear()
    #             lcd.message("TO1 Hz: %.2f" % (0))
    #             lcd2.clear()
    #             lcd2.message("TO2 Hz: %.2f" % (0))
    #         sleep(0.05)
    # return received_data

    app.run()
