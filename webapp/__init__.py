from . import mqtt_client

# TODO: fix dat sh1t
if not hasattr(mqtt_client, 'property'):
    mqtt_client.property = "running"
    mqtt_client.client.loop_start()
