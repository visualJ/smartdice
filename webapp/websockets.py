from channels import Group


def ws_connect(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    Group("update").add(message.reply_channel)


def ws_disconnect(message):
    Group("update").discard(message.reply_channel)


def ws_send_update():
    Group("update").send({'text': 'update'})
