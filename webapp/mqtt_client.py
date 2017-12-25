import paho.mqtt.client as mqtt

MQTT_BROKER_KEEPALIVE = 60
MQTT_BROKER_PORT = 1883
MQTT_BROKER_HOST = "test.mosquitto.org"
SMARTDICE_TOPIC = 'smartdice'


def on_connect(cl, userdata, flags, rc):
    cl.subscribe(SMARTDICE_TOPIC + "/+/+")


def on_message_dice(dice_number, topic, message):
    print("{}: {}".format(dice_number, message))


_on_message_dice = on_message_dice
client = mqtt.Client()


def on_message(client, userdata, msg):
    try:
        topic_parts = msg.topic.split('/')
        dice_number = int(topic_parts[1])
        topic = topic_parts[2]
        message = str(msg.payload, encoding="UTF-8")
    except ValueError and IndexError:
        pass
    else:
        _on_message_dice(dice_number, topic, message)


def receive_mqtt_dice_messages(func):
    global _on_message_dice
    _on_message_dice = func
    return func


def publish_message_dice(dice_number, topic, message):
    client.publish('{}/{}/{}'.format(SMARTDICE_TOPIC, dice_number, topic), message)


def connect_client():
    global client
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_BROKER_KEEPALIVE)
    client.loop_start()
