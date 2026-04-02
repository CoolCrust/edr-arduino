#include <EEPROM.h>
const int potPin = A0;
const int crashPin = 2;
void setup() {
  Serial.begin(9600);
  pinMode(crashPin, INPUT_PULLUP);
}
void loop() {
  int throttle = analogRead(potPin);
  int crashState = digitalRead(crashPin);
  Serial.print(throttle);
  Serial.print(",");
  Serial.println(crashState);
  delay(100);
}
