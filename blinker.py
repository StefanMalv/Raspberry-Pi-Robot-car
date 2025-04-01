# Blinker of Rasberry Pi
import RPi.GPIO as GPIO
from time import sleep
from reciver import input_

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

BLINK_DURATION = 0.6 
GAP_DURATION = 0.2 

# Maps color, direction and distance to our protocol
def main():
   # color, direction, distance = position
   
    position = input_()

    color, direction, distance = position[0], position[1], position[2]

    map_color(color)
    sleep(1)
    map_direction(direction)
    sleep(1)
    map_distance(distance)
    sleep(1)
    

# Finds the color
def map_color(color): 
    if color == 3:
        blink()
        
    elif color == 1:
        blink(2)
        
    elif color == 4:
        blink(3)
        
    elif color == 2:
        blink(4)
        
# Finds direction  
def map_direction(direction):
    if direction == 1:
        blink(1)
    
    if direction == 3:
        blink(2)
        
    if direction == 2:
        blink(3)

# Finds distance
def map_distance(distance):
    if distance == "far":
        blink(2)
        
    if distance == "close":
        blink()

# Function for blinking  
def blink(iterations=1):
    for _ in range(iterations):
        GPIO.output(pin, GPIO.HIGH)
        sleep(BLINK_DURATION)
        GPIO.output(pin, GPIO.LOW)
        sleep(GAP_DURATION)
    
    
if __name__ == "__main__":
    main()

    
    
            