import serial
import time

arduino_port = 'COM7'  
ser = serial.Serial(arduino_port, 9600, timeout=1)

def send_command(command):
    ser.write(command.encode())

def main():
    try:
        while True:
            user_input = input("Enter '0' for one direction or '1' for the other: ")
            if user_input == '0' or user_input == '1':
                send_command(user_input)
                time.sleep(1)  # Delay for a second
            else:
                print("Invalid input. Please enter '0' or '1'.")
    except KeyboardInterrupt:
        print("Script terminated by user.")
    finally:
        ser.close()  # Close the serial connection

if __name__ == "__main__":
    main()
