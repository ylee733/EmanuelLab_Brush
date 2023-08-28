int pwmPin = 9; // speed control pin
int RPin = 8;   // direction pin for one side of the motor
int LPin = 7;   // direction pin for the other side of the motor

void setup() {
  pinMode(pwmPin, OUTPUT);
  pinMode(RPin, OUTPUT);
  pinMode(LPin, OUTPUT);

  digitalWrite(RPin, LOW);
  digitalWrite(LPin, LOW);
  randomSeed(analogRead(0));

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '0') {
      digitalWrite(RPin, HIGH);
      digitalWrite(LPin, LOW);
      delay(1000);
    } else if (command == '1') {
      digitalWrite(RPin, LOW);
      digitalWrite(LPin, HIGH);
    } else {
      digitalWrite(RPin, LOW);
      digitalWrite(LPin, LOW);
    }
      digitalWrite(RPin, LOW);
      digitalWrite(LPin, LOW);
      delay(1000);
    analogWrite(pwmPin, 255);
  }
}
