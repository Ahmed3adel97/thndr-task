
import paho.mqtt.client as mqtt
import json
import time

time.sleep(10)
data = {}
def on_connect(client, userdata, flags, rc):

    client.subscribe([("thndr-trading", 1)])



def on_message(client, userdata, message):

    stock = json.loads(message.payload)
    data[stock['stock_id']] = stock

    
broker_address = "vernemq"
port = 1883

client = mqtt.Client() 
client.on_connect = on_connect  
client.on_message = on_message  

client.connect(broker_address, port=port)  # connect to broker

client.loop_forever()
print(2)