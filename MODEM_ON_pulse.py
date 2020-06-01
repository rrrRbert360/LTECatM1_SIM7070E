#####################################################################################################################################################################################
#
# Piece-of-Cake Modem debug tooling | Robert J. Heerekop IOTC360 May 2020
# Read Piece-of-Cake Manual (!)
#
# The gpio21 is used to switch on/off the USB connected modem.
# The gpio21 output is normally 3v3 and for 2sec low to generate a pulse. 
#
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#####################################################################################################################################################################################
#
# Set the GPIO-pin high/low/float
#
def GPTurn(Action):
    if Action == "high":
	GPIO.setup(21,GPIO.OUT)
	GPIO.output(21,1)

    if Action == "low":
	GPIO.setup(21,GPIO.OUT)
	GPIO.output(21,0)

    if Action == "float":
	GPIO.setup(21,GPIO.IN)

print "gpio21 low for 2s"
GPTurn("low")
time.sleep(2)
print "high again"
GPTurn("high")
