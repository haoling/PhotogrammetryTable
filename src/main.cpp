#include <Arduino.h>
#include <VarSpeedServo.h>
VarSpeedServo myservo;

#define PIN_SERVO 9
#define SPEED 30

void setup() {
    myservo.attach(PIN_SERVO);
}

void loop (){
    myservo.write(180, SPEED, true);
    myservo.wait();
    delay(200);
    myservo.write(0, SPEED, true);
    myservo.wait();
    delay(1000);
}