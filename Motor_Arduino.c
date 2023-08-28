int pwnPin = 9; // speed control pin
int RPin = 8; // direction pin
int LPin = 7; // direction pin

void setup() {
  pinMode(pwnPin, OUTPUT);
  pinMode(RPin, OUTPUT);
  pinMode(LPin, OUTPUT);

  digitalWrite(RPin, LOW);
  digitalWrite(LPin, LOW);
  randomSeed(analogRead(0));

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  int randomNum = random(2);
  Serial.println(randomNum);

  analogWrite(pwnPin, 255);
 
    if (randomNum == 0) {
      digitalWrite(RPin, HIGH);
      digitalWrite(LPin, LOW);
      delay(1000);
    } else {
      digitalWrite(RPin, LOW);
      digitalWrite(LPin, HIGH);
      delay(1000);
    }
    digitalWrite(RPin, LOW);
    digitalWrite(LPin, LOW);
    delay(1000);
  
}

