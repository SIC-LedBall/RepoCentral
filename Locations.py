import paho.mqtt.client as mqtt

topicPlayer1 = "lbplayer1"
topicPlayer2 = "lbplayer2"
topicBall = "lbball"

livesPlayer1 = 3
ballHit = "nohit"


def on_connect(client, userdate, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topicPlayer1)
    client.subscribe(topicPlayer2)
    client.subscribe(topicBall)
    client.publish(topicPlayer1, "hit;3")

def on_message(client, userdate, msg):
    #print(msg.topic + " " + str(msg.payload))

    if(msg.topic == topicPlayer1):
        payload = msg.payload
        print(msg.topic + " - " + payload)

    if (msg.topic == topicPlayer2):
        payload = msg.payload
        print(msg.topic + " - " + payload)

    if(msg.topic == topicBall):
        global ballHit
        payload = msg.payload

        if(payload == "hit"):
            ballHit = msg.payload
            global livesPlayer1
            livesPlayer1 -= 1
            hitPlayer(ballHit, topicPlayer1, str(livesPlayer1))

        if(payload == "reset"):
            livesPlayer1 = 4

        print(msg.topic + " - " + ballHit)




def hitPlayer(ballHit, playerTopic, playerLives):
    client.publish(str(playerTopic), str(ballHit + ";" + playerLives))
    print(ballHit + ";" + playerLives)

client = mqtt.Client()
client.connect("192.168.1.200", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()