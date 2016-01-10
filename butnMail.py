import RPi.GPIO as GPIO ## Import library that lets you control the Pi's GPIO pins
from time import sleep ## Import time for delays
 
## Import the ISStreamer module
from ISStreamer.Streamer import Streamer
 
## Streamer constructor, this will create a bucket called Double Button LED
streamer = Streamer(bucket_name="Double Button LED", access_key="[Place Your Access Key Here]")
 
GPIO.setwarnings(False) ## Disables messages about GPIO pins already being in use
GPIO.setmode(GPIO.BOARD) ## Indicates which pin numbering configuration to use
 
GPIO.setup(16, GPIO.IN) ## Tells it that pin 16 (button) will be giving input
GPIO.setup(18, GPIO.IN) ## Tells it that pin 18 (button) will be giving input
 
GPIO.setup(7, GPIO.OUT) ## Tells it that pin 7 (LED) will be outputting
GPIO.setup(11, GPIO.OUT) ## Tells it that pin 11 (LED) will be outputting
GPIO.setup(13, GPIO.OUT) ## Tells it that pin 13 (LED) will be outputting
GPIO.output(7, GPIO.HIGH) ## Sets pin 7 (LED) to "HIGH" or off
GPIO.output(11, GPIO.HIGH) ## Sets pin 11 (LED) to "HIGH" or off
GPIO.output(13, GPIO.HIGH) ## Sets pin 13 (LED) to "HIGH" or off

## state - decides what LED should be on and off
## if mail is not sent, yellow.. if mail sent, green
## initialize to 0 or all off
state = 0
sent = 0 

## This while loop constantly looks for button input (presses)
while True:
 
    ## When state toggle button is pressed
    if ( GPIO.input(16) == True ):
 
        ########################SEND EMAIL################################
		
		##################################################################
		if (sent):
			GPIO.output(7, GPIO.HIGH) ## LED on.. indicates email sent
            GPIO.output(11, GPIO.LOW) ## LED off
            print 
		else:
			GPIO.output(7, GPIO.LOW) ## LED off
            GPIO.output(11, GPIO.HIGH) ## LED on.. indicates email not sent
