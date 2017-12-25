from . import mqtt_client

if not hasattr(mqtt_client, 'property'):
    mqtt_client.property = "running"
    mqtt_client.connect_client()
