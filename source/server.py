import paho.mqtt.client as mqtt
import json
from datetime import datetime
import time

BROKER = "dev.rightech.io"
PORT = 1883
CLIENT_ID = "mqtt-acry_wxrk-obj2"
TOPIC_SENSOR = f"devices/{CLIENT_ID}/state"
TOPIC_MODE = f"devices/{CLIENT_ID}/commands/mode"
TOPIC_ACTUATOR = f"devices/{CLIENT_ID}/commands/actuator"

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
manual_mode = None
actuator_mode = False
fire_suppression_status = None  # ссылка на функцию для активации пожаротушения
start_time = time.time()

def get_actuator_mode():
    global actuator_mode
    return actuator_mode

def set_actuator_mode(var):
    global actuator_mode
    actuator_mode = var

def set_manual_mode(var):
    global manual_mode
    manual_mode = var

def publish_sensor_data(smoke_level):

    rounded_smoke_level = round(smoke_level, 1)

    client.publish(TOPIC_SENSOR, payload=rounded_smoke_level)

def set_fire_suppression_status(status_func):
    global fire_suppression_status
    fire_suppression_status = status_func  # функция для управления пожаротушением из main.py

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_MODE)
    client.subscribe(TOPIC_ACTUATOR)

def on_message(client, userdata, msg):
    global manual_mode
    payload = msg.payload.decode()
    if msg.topic == TOPIC_MODE:
        if payload == "auto":
            if manual_mode == 0:
                print("Автоматический режим УЖЕ включен")
            else:
                set_manual_mode(0)
                print("Автоматический режим включен")
        elif payload == "manual":
            if manual_mode == 1:
                print("Ручной режим УЖЕ включен")
            else:
                set_manual_mode(1)
                print("Ручной режим включен")

    elif msg.topic == TOPIC_ACTUATOR:
        if payload == "activate":
            if manual_mode:
                print("Актуатор активирован по команде от сервера")
                set_actuator_mode(True)
            else:
                print('Невозможно включить актуатор, включен автоматический режим')


client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()
