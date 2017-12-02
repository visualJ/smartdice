import paho.mqtt.client as mqtt

# from webapp.models import RollResult, SmartDice

TOPIC_PREFIX_SEPARATOR = ":"
SMARTDICE_TOPIC_PREFIX = "smartdice"


def on_connect(cl, userdata, flags, rc):
    # resubscribe if connection was lost
    cl.subscribe("$SYS/#")


def on_message_dice(dice_number, message):
    print("{}: {}".format(dice_number, message))


_on_message_dice = on_message_dice


def on_message(client, userdata, msg):
    # print("{}: {}".format(msg.topic, msg.payload))
    if msg.topic.startswith(SMARTDICE_TOPIC_PREFIX + TOPIC_PREFIX_SEPARATOR):
        dice_number = int(msg.topic.split(TOPIC_PREFIX_SEPARATOR)[1])
        _on_message_dice(dice_number, msg.payload)


# dice = SmartDice.objects.get(dice_number=dice_number)
# if dice:
#    result = RollResult(mode='D6', value=1, user=dice.session.active_user, session=dice.session)
#    result.save()


def set_on_message_dice(func):
    global _on_message_dice
    _on_message_dice = func


def subscribe_dice(dice_number):
    client.subscribe(SMARTDICE_TOPIC_PREFIX + TOPIC_PREFIX_SEPARATOR + str(dice_number))


def unsubscribe_dice(dice_number):
    client.unsubscribe(SMARTDICE_TOPIC_PREFIX + TOPIC_PREFIX_SEPARATOR + str(dice_number))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
