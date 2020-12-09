import socket
import RPi.GPIO as GPIO
import time
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(8,GPIO.OUT)
servo1 = GPIO.PWM(8,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

toggle=True;

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    with clientsocket:
        while True:
            try:
                x = clientsocket.recv(1024).decode()
                if x:
                    if toggle:
                        print("ON")
                        toggle = False
                        servo1.ChangeDutyCycle(7)
                        time.sleep(0.3)
                        servo1.ChangeDutyCycle(0)
                    else:
                        print("OFF")
                        toggle = True
                        servo1.ChangeDutyCycle(2)
                        time.sleep(0.3)
                        servo1.ChangeDutyCycle(0)
            except:
                print("Client Disconnected")
                break
            print(x)
            if not x:
                print("Client Disconnected")
                break
            
