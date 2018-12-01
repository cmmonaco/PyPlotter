// Arduino Serial Interface to MAX6675 Thermocouple Amplifier
// Simply returns temperature reading in Celcius to read by another program.

#include "max6675.h"

// Data and control lines
int thermoDO = 4;
int thermoCS = 5;
int thermoCLK = 6;

// Initialize thermocouple amp
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);
  
void setup() {
  Serial.begin(9600);
  delay(1000);
}

void loop() {

   // Print temperature reading once every 250ms
   Serial.println(thermocouple.readCelsius());
   delay(250);
}
