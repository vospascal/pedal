// 11-10-2020
#include <Joystick.h>  // Using the lib included with SimHub originally from Matthew Heironimus
#include "multimap.h"


Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_GAMEPAD,
                   0, 0,                  // Button Count, Hat Switch Count
                   false, false, false,     // X and Y, but no Z Axis
                   false, false, false,   // No Rx, Ry, or Rz
                   true, true,          // No rudder or throttle
                   false, true, false);  // No accelerator, brake, or steering


//const bool initAutoSendState = true;
int throttleValue = 0;
int brakeValue = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Joystick.begin();
  Joystick.setThrottle(throttleValue);
  Joystick.setBrake(brakeValue);
  delay(200);
}


float inputMap[] =  { 0, 20, 40, 60, 80, 100 };
float outputMap[] = { 0, 15, 43, 53, 75, 100 };

// the loop routine runs over and over again forever:
void loop() {

//  if (Serial.available() > 0) {
//    // read the incoming byte:
//    incomingByte = Serial.read();
//
//    // say what you got:
//    Serial.print("I received: ");
//    Serial.println(incomingByte, DEC);
//  }
  
  // read the input on analog pin 0:
  int throttleRawValue = analogRead(A0);
  int brakeRawValue = analogRead(A1);
  float T;
  float B;
  // print out the value you read:

  if (throttleRawValue <= 74) {
//    Serial.print(0);
    T = abs(0);
    Joystick.setThrottle(abs(0));
//    Joystick.sendState(); // Update the Joystick status on the PC
  } else {
    float restThrottleValue = throttleRawValue - 74;
    Joystick.setThrottle(restThrottleValue);
    T = multiMap<float>(restThrottleValue/4, inputMap, outputMap, 100);
//    T = restThrottleValue;
//    Serial.print(restThrottleValue);
//    Joystick.sendState(); // Update the Joystick status on the PC
  }


  if (brakeRawValue <= 74) {
//    Serial.println(0);
    B = abs(0);
    Joystick.setBrake(abs(0));
//    Joystick.sendState(); // Update the Joystick status on the PC
  } else {
    float restBrakeValue = brakeRawValue - 74;
    Joystick.setBrake(restBrakeValue);
    B= multiMap<float>(restBrakeValue/4, inputMap, outputMap, 100);
//    B = restBrakeValue;
//    Serial.println(restBrakeValue);
//    Joystick.sendState(); // Update the Joystick status on the PC
  }
  Serial.print("T:");
  Serial.println(T); 
  Serial.print("B:");
  Serial.println(B);

  Joystick.sendState(); // Update the Joystick status on the PC
  Serial.flush();
  delay(10);
}
