from machine import Pin,UART
import utime
import json
import urandom 
import gc

solenoid = Pin(0, Pin.OUT, Pin.PULL_DOWN)
lick = Pin(1, Pin.IN, Pin.PULL_DOWN)
# timestamps = []
count = 0
count_stim = 0
file_path = '/phase2.json'

try:
    with open(file_path, "r") as file:
        data = json.load(file)
except OSError as e:
    print(e.args[0])
    if e.args[0] == 2:  
        data = []
    else:
        raise

led = Pin("LED", Pin.OUT)
to_arduino = Pin(6, Pin.OUT)

solenoid_active = False
# solenoid.value(1)
# utime.sleep(0.05)
# solenoid.value(0)
valve_T0 = utime.ticks_ms()
valve_time = utime.ticks_ms() - valve_T0
valve_time_abs = utime.ticks_ms()
stim_T0 = utime.ticks_ms()
iti = urandom.randint(5000, 10000)

# create stim record

try:
    while True:      
        #light off arduino
        if utime.ticks_diff(utime.ticks_ms(), stim_T0) > iti:
            stim_T0 = utime.ticks_ms()
            stim_time = utime.ticks_diff(stim_T0, valve_T0)
            to_arduino.value(0)
            utime.sleep(.05)
            to_arduino.value(1)
            count_stim =+ 1
            iti = urandom.randint(5000, 10000)
            data_entry = {
                "lick": "N/A",
                "Counter": "N/A",
                "Valve": "N/A",
                "Stim" : stim_time
            }
            
            data.append(data_entry)

            with open(file_path, 'a') as file:
                file.write(json.dumps(data_entry) + '\n')
            print(data)
            print("counter:", count)

        gc.collect()
        
        
        if lick.value(): 
            lick_time = utime.ticks_ms() - valve_T0 
            solenoid_active = True
            #valve_time = "null"
            utime.sleep(0.01)

            # when lick
            led.value(1)
            if solenoid_active == True and (utime.ticks_diff(utime.ticks_ms(), stim_T0) <= 1000) and (utime.ticks_diff(utime.ticks_ms(), valve_time_abs) > 4000):
                print(utime.ticks_ms() - valve_T0 - valve_time)
                count += 1
                #if lick.value():
                solenoid.value(1)
                valve_time_abs = utime.ticks_ms()
                valve_time = utime.ticks_diff(valve_time_abs, valve_T0)
                utime.sleep(0.05)
                solenoid.value(0)
                solenoid_active = False
            
                
            data_entry = {
                "lick": lick_time,
                "Counter": count,
                "Valve": valve_time,
                "Stim" : "N/A"
            }
            
            data.append(data_entry)

            with open(file_path, 'a') as file:
                file.write(json.dumps(data_entry) + '\n')
            print(data)
            print("counter:", count)

        gc.collect()
        
except KeyboardInterrupt:
    pass

