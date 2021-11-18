#include <Wire.h>
#include "MAX30105.h"

// Pins.
const int sda1Pin = 27;
const int scl1Pin = 26;
const int sda2Pin = 33;
const int scl2Pin = 32;
const int ecgPin = 36;

// I2C.
TwoWire i2c1 = TwoWire(0);
TwoWire i2c2 = TwoWire(1);

// PPG sensors.
MAX30105 ppg1;
MAX30105 ppg2;

// Sampling frequency.
const int fs = 100;

unsigned long currentTime;
unsigned long sampleTime;
int ecg;
long ppg1Ir;
long ppg1Red;
long ppg1Green;
long ppg2Ir;
long ppg2Red;
long ppg2Green;
unsigned long ecgTimestamp;
unsigned long ppg1Timestamp;
unsigned long ppg2Timestamp;

void setup() {
  // Initialize serial communication.
  Serial.begin(115200);
  // Wait for the serial port to open.
  while (!Serial);

  // Initialize I2C.
  i2c1.begin(sda1Pin, scl1Pin);
  i2c2.begin(sda2Pin, scl2Pin);
  
  // Initialize PPG1 sensor.
  //Serial.print("Initializing PPG1...");
  if (!ppg1.begin(i2c1, I2C_SPEED_FAST))
  {
    //Serial.println("PPG1 not found.");
    while (1);
  }
  //Serial.println("PPG1 found.");

  // Initialize PPG2 sensor.
  //Serial.print("Initializing PPG2...");
  if (!ppg2.begin(i2c2, I2C_SPEED_FAST))
  {
    //Serial.println("PPG2 not found.");
    while (1);
  }
  //Serial.println("PPG2 found.");

  // Configure PPG1.
  ppg1.setup();
  // Turn the red LED off.
  ppg1.setPulseAmplitudeRed(0x00);
  ppg1.setSampleRate(0x0C);
  ppg1.setFIFOAverage(0x04);

  // Configure PPG2.
  ppg2.setup();
  // Turn the red LED off.
  ppg2.setPulseAmplitudeRed(0x00);
  ppg2.setSampleRate(0x0C);
  ppg2.setFIFOAverage(0x04);

  sampleTime = millis() + 1000 / fs;
}

void loop() {
  currentTime = millis();
  if (currentTime >= sampleTime) {
    sampleTime = currentTime + 1000 / fs;

    // ECG.
    ecg = analogRead(ecgPin);
    ecgTimestamp = millis();

    // PPG1 readings.
    ppg1Ir = ppg1.getIR();
    ppg1Red = ppg1.getRed();
    ppg1Green = ppg1.getGreen();
    ppg1Timestamp = millis();

    // PPG2 readings.
    ppg2Ir = ppg2.getIR();
    ppg2Red = ppg2.getRed();
    ppg2Green = ppg2.getGreen();
    ppg2Timestamp = millis();

    // Serial communication.
    Serial.print(ecgTimestamp);
    Serial.print(",");
    Serial.print(ecg);
    Serial.print(",");
    Serial.print(ppg1Timestamp);
    Serial.print(",");
    Serial.print(ppg1Ir);
    Serial.print(",");
    Serial.print(ppg1Red);
    Serial.print(",");
    Serial.print(ppg1Green);
    Serial.print(",");
    Serial.print(ppg2Timestamp);
    Serial.print(",");
    Serial.print(ppg2Ir);
    Serial.print(",");
    Serial.print(ppg2Red);
    Serial.print(",");
    Serial.println(ppg2Green);
  }
}
