from machine import Pin, UART
import utime
import json
import random  
import gc

solenoid = Pin(0, Pin.OUT, Pin.PULL_DOWN)
lick = Pin(1, Pin.IN, Pin.PULL_DOWN)
count = 0
count_stim = 0
file_path = '/nov_21_test1234567896891142.json'

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
direction2_pin = Pin(4, Pin.OUT)
direction1_pin = Pin(5, Pin.OUT)

solenoid_active = False
valve_T0 = utime.ticks_ms()
valve_time = utime.ticks_ms() - valve_T0
valve_time_abs = utime.ticks_ms()
stim_T0 = utime.ticks_ms()
iti = random.randint(5000, 10000)  # time between trials is randomly 5 to 10 seconds

try:
    while True:
        # random bit
        direction = random.choice([0, 1])

        if utime.ticks_diff(utime.ticks_ms(), stim_T0) > iti:
            stim_T0 = utime.ticks_ms()
            stim_time = utime.ticks_diff(stim_T0, valve_T0)

            # Set the direction pin before sending the stimulus
            if direction:
                direction1_pin.value(0)
            else:
                direction2_pin.value(0)
            utime.sleep(0.05)
            direction1_pin.value(1)
            direction2_pin.value(1)
            count_stim += 1
            iti = random.randint(5000, 10000)
            data_entry = {
                "lick": "N/A",
                "Counter": "N/A",
                "Valve": "N/A",
                "Stim": stim_time
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
            utime.sleep(0.01)

            led.value(1)
            if solenoid_active and (
                    utime.ticks_diff(utime.ticks_ms(), stim_T0) <= 1000) and (
                    utime.ticks_diff(utime.ticks_ms(), valve_time_abs) > 4000):
                print(utime.ticks_ms() - valve_T0 - valve_time)
                count += 1
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
                "Stim": "N/A"
            }

            data.append(data_entry)

            with open(file_path, 'a') as file:
                file.write(json.dumps(data_entry) + '\n')
            print(data)
            print("counter:", count)

        gc.collect()

except KeyboardInterrupt:
    pass

