import paho.mqtt.client as mqtt


def on_connect(self,client, userdata, rc):
    print("subscribed to topic")


def on_message(client, userdata, msg):
    # Do something
    print(msg.payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("leeroy")
