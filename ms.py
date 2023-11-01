import utime
import json
from machine import Pin
import urandom 
import gc

solenoid = Pin(0, Pin.OUT, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
lick = Pin(1, Pin.IN, Pin.PULL_DOWN)
timestamps = []
count = 0
file_path = '/BAX2wednesday.json'

try:
    with open(file_path, "r") as file:
        data = json.load(file)
except OSError as e:
    print(e.args[0])
    if e.args[0] == 2:  
        data = []
    else:
        raise


solenoid_active = False
solenoid.value(1)
utime.sleep(0.05)
solenoid.value(0)
valve_T0 = utime.ticks_ms()
valve_time = utime.ticks_ms() - valve_T0  

try:
    while True:
        #valve_T0 = utime.ticks_ms()
        if lick.value(): 
            lick_time = utime.ticks_ms() - valve_T0 
            solenoid_active = True
            #valve_time = "null"
            utime.sleep(0.01)

            # when lick
            led.value(1)
            if solenoid_active == True and ((utime.ticks_ms() - valve_T0 - valve_time) >= urandom.randint(5000, 10000)):
                print(utime.ticks_ms() - valve_T0 - valve_time)
                count += 1
                #if lick.value():
                solenoid.value(1)
                valve_time = utime.ticks_ms() - valve_T0 
                utime.sleep(0.05)
                solenoid.value(0)
                solenoid_active = False
            
                
            data_entry = {
                "lick": lick_time,
                "Counter": count,
                "Valve": valve_time,
            }
            data.append(data_entry)

            with open(file_path, 'a') as file:
                file.write(json.dumps(data_entry) + '\n')
            print(data)
            print("counter:", count)

        gc.collect()
        
except KeyboardInterrupt:
    pass

