import os, logging
import paho.mqtt.client as mqtt

def not_empty(string):
    return string != ''

def on_connect(client, userdata, flags, rc):
    logger.info('Connected')
    client.subscribe(ROBOT + '/#')

def on_message(client, userdata, msg):
    message = str(msg.payload.decode('utf-8'))
    logger.info('RECEIVED ' + msg.topic + ' ' + message)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.loop_forever()

if __name__ == '__main__':
    ROBOT = os.getenv('ROBOT', 'julinho')
    BROKER = os.getenv('MQTT_BROKER', 'mqtt.sj.ifsc.edu.br')

    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    main()
