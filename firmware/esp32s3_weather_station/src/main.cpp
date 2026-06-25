#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(1000);

  Serial.println("Smart Weather Station AI Lab");
  Serial.println("ESP32-S3 environment is working");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Waiting for sensors...");
  delay(2000);
}

