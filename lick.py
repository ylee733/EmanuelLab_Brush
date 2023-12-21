import utime
import ujson
from machine import Pin
solenoid = Pin(0, Pin.OUT, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
lick = Pin(14, Pin.IN, Pin.PULL_DOWN)
timestamps = []

try:
    while True:
        if lick.value() == 1: 
            timestamp = utime.time() 
            formatted_time = utime.localtime(timestamp)
            print("Lick detected at: {}/{}/{} {}:{}:{}".format(formatted_time[2], formatted_time[1], formatted_time[0], formatted_time[3], formatted_time[4], formatted_time[5]))
            led.value(1)
        else:
            led.value(0)
        
except KeyboardInterrupt:
    pass  
finally:
        lick.value(0) 
