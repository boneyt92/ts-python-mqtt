from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import config

string.alphanum='1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

channelID = config.channelID
writeAPIKey = config.writeAPIKey
mqttHost = config.mqttHost
mqttUsername = config.mqttUsername
mqttAPIKey = config.mqttAPIKey
tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

while(1):

    clientID = ''

# Create a random clientID.
    for x in range(1,16):
        clientID+=random.choice(string.alphanum)

    # get the system performance data over 20 seconds.
    cpuPercent = psutil.cpu_percent(interval=10)
    ramPercent = psutil.virtual_memory().percent

    # build the payload string.
    payload = "field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)


    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
	print (" Published CPU =",cpuPercent," RAM =", ramPercent," to host: " , mqttHost , " clientID= " , clientID)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")