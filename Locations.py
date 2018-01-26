import paho.mqtt.client as mqtt

topicPlayer1 = "lbplayer1"
topicPlayer2 = "lbplayer2"
topicBall = "lbball"

def on_connect(client, userdate, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topicPlayer1)
    client.subscribe(topicPlayer2)
    client.subscribe(topicBall)


def on_message(client, userdate, msg):
    #print(msg.topic + " " + str(msg.payload))

    if(msg.topic == topicPlayer1):
        payload = msg.payload
        print(msg.topic + " - " + payload)

    if (msg.topic == topicPlayer2):
        payload = msg.payload
        print(msg.topic + " - " + payload)

    if(msg.topic == topicBall):
        payload = msg.payload
        print(msg.topic + " - " + payload)


client = mqtt.Client()
client.connect("192.168.1.200", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()