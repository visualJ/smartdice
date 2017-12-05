import paho.mqtt.client as mqtt

MQTT_BROKER_KEEPALIVE = 60
MQTT_BROKER_PORT = 1883
MQTT_BROKER_HOST = "test.mosquitto.org"
SMARTDICE_TOPIC = 'smartdice'


def on_connect(cl, userdata, flags, rc):
    cl.subscribe(SMARTDICE_TOPIC + "/#")


def on_message_dice(dice_number, message):
    print("{}: {}".format(dice_number, message))


_on_message_dice = on_message_dice


def on_message(client, userdata, msg):
    if msg.topic.startswith(SMARTDICE_TOPIC):
        dice_number = int(msg.topic.split('/')[1])
        _on_message_dice(dice_number, msg.payload)


def receive_mqtt_dice_messages(func):
    global _on_message_dice
    _on_message_dice = func
    return func


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_BROKER_KEEPALIVE)
