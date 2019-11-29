import pyfirmata
import time
import serial
from twilio.rest import Client

ArduinoSerial=serial.Serial('COM3',9600)

time.sleep(2)
while 1:
        var=ArduinoSerial.readline()
        print(var)
        lim=str(var)
        lim1=lim[2]
        print(lim1)
        if (lim1=='1'):
                # Your Account SID from twilio.com/console
                account_sid = "ACbc5d4af16e45a137c1f484fe43edcd27"
                # Your Auth Token from twilio.com/console
                auth_token  = "e1132767f44783c9c7d23040985164a2"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                        to="+917503256028", 
                        from_="+12055579487",
                        body="Bijendar is drunk")

                print(message.sid)
                time.sleep(180)
"""Credits to twilio, circuitdigest"""
