// 11-10-2020
#include <Joystick.h>  // Using the lib included with SimHub originally from Matthew Heironimus
#include "MultiMap.h"


Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_GAMEPAD,
                   0, 0,                  // Button Count, Hat Switch Count
                   false, false, false,     // X and Y, but no Z Axis
                   false, false, false,   // No Rx, Ry, or Rz
                   true, true,          // No rudder or throttle
                   false, true, false);  // No accelerator, brake, or steering


//const bool initAutoSendState = true;
int throttleValue = 0;
int brakeValue = 0;
int clutchValue = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Joystick.begin();
  Joystick.setThrottle(throttleValue);
  Joystick.setBrake(brakeValue);
//  Joystick.setAccelerator(clutchValue);
  delay(2000);
}


int inputMapClutch[] =  { 0, 20, 40, 60, 80, 100 };
int outputMapClutch[] = { 0, 15, 43, 53, 75, 100 };

int inputMapThrottle[] =  { 0, 20, 40, 60, 80, 100 };
int outputMapThrottle[] = { 0, 15, 43, 53, 75, 100 };


int inputMapBrake[] =  { 0, 20, 40, 60, 80, 100 };
int outputMapBrake[] = { 0, 15, 43, 53, 75, 100 };

int BrakeBefore;
float BrakeAfter;

int ThrottleBefore;
float ThrottleAfter;


//int ClutchBefore;
//float ClutchAfter;

// the loop routine runs over and over again forever:
void loop() {

  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'd')
    {
      String TMAP = "TMAP:" + String(outputMapThrottle[0]) + "-" + String(outputMapThrottle[1]) + "-" + String(outputMapThrottle[2]) + "-" + String(outputMapThrottle[3]) + "-" + String(outputMapThrottle[4]) + "-" + String(outputMapThrottle[5]);
      Serial.print(TMAP);
      Serial.println(',');

      String BMAP = "BMAP:" + String(outputMapBrake[0]) + "-" + String(outputMapBrake[1]) + "-" + String(outputMapBrake[2]) + "-" + String(outputMapBrake[3]) + "-" + String(outputMapBrake[4]) + "-" + String(outputMapBrake[5]);
      Serial.print(BMAP);
      Serial.println(',');

      String CMAP = "CMAP:" + String(outputMapClutch[0]) + "-" + String(outputMapClutch[1]) + "-" + String(outputMapClutch[2]) + "-" + String(outputMapClutch[3]) + "-" + String(outputMapClutch[4]) + "-" + String(outputMapClutch[5]);
      Serial.print(CMAP);
      Serial.println(',');
    }

    delay(50);
    
    if (c == 'e'){
      Serial.print("setMap called");
      Serial.println(',');
    }

  }


  // read the input on analog pin 0:
  int throttleRawValue = analogRead(A0);
  int brakeRawValue = analogRead(A1);
//  int clutchRawValue = analogRead(A2);
  
  // print out the value you read:
  //
  if (throttleRawValue <= 74) {
    ThrottleBefore = 0;
    ThrottleAfter = 0;
    Joystick.setThrottle(0);
  } else {
    int restThrottleValue = throttleRawValue - 74;

    ThrottleBefore = restThrottleValue / 4;
    ThrottleAfter = multiMap<int>(ThrottleBefore, inputMapThrottle, outputMapThrottle, 50);
    Joystick.setThrottle(ThrottleAfter);
  }

  if (brakeRawValue <= 74) {
    BrakeBefore = 0;
    BrakeAfter = 0;
    Joystick.setBrake(0);
  } else {
    int restBrakeValue = brakeRawValue - 74;

    BrakeBefore = restBrakeValue / 4;
    BrakeAfter = multiMap<int>(BrakeBefore, inputMapBrake, outputMapBrake, 50);
    Joystick.setBrake(BrakeAfter);
  }

//  if (clutchRawValue <= 74) {
//    ClutchBefore = 0;
//    ClutchAfter = 0;
//    Joystick.setAccelerator(0);
//  } else {
//    int restClutchValue = clutchRawValue - 74;
//
//    ClutchBefore = restClutchValue / 4;
//    ClutchAfter = multiMap<int>(ClutchBefore, inputMapClutch, outputMapClutch, 50);
//    Joystick.setAccelerator(ClutchAfter);
//  }

  
  String p1 = ";";
  Serial.print("T:");
  Serial.println(ThrottleBefore + p1 + ThrottleAfter);

  Serial.print("B:");
  Serial.println(BrakeBefore + p1 + BrakeAfter);
//
//  Serial.print("C:");
//  Serial.println(ClutchBefore + p1 + ClutchAfter);
  
  Joystick.sendState(); // Update the Joystick status on the PC
  Serial.flush();
  delay(100);
}
