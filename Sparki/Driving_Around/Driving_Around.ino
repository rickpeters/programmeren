/*******************************************
 * Edge Avoidance
 * 
 * Sparki has an array of infrared sensors
 * underneath. It can use these to detect
 * if there is anything underneath it. 
 * 
 * This program detects if Sparki is about to
 * fall off the edge. If it is, it turns the
 * other way before continuing.
 * 
 ********************************************/

#include <Sparki.h> // include the sparki library

void setup()
{       
  sparki.servo(SERVO_CENTER); // center the servo
}

// constants and initialization
const int NONE  = 0;
const int LEFT  = 1;
const int RIGHT = 2;
const int WALL_TURN = 45;
const int WALL_BACK = 3;
const int EDGE_TURN = 100;
const int EDGE_BACK = 2;
int edge = NONE;
int program = false;

// helper functions
void EdgeAvoidance() {
  // edge avoidance
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor

  int threshold = 200; // if below this value, no surface underneath

  if (edgeLeft < threshold) // if no surface underneath left sensor
  {
    edge = LEFT;
    sparki.RGB(RGB_BLUE); // turn the led blue
    sparki.moveBackward(EDGE_BACK); // move back a bit
    sparki.moveRight(EDGE_TURN); // turn right
  }

  if (edgeRight < threshold) // if no surface underneath right sensor
  {
    edge = RIGHT;
    sparki.RGB(RGB_BLUE); // turn the led blue
    sparki.moveBackward(2); // move back a bit
    sparki.moveLeft(EDGE_TURN); // turn left
  }
}

void WallAvoidance() {
  // wall avoidance
  int cm = sparki.ping(); // measures the distance with Sparki's eyes

  if(cm != -1) // make sure its not too close or too far
  { 
    if(cm < 20) // if the distance measured is less than 20 centimeters
    {
      sparki.RGB(RGB_RED); // turn the led red
      sparki.beep(); // beep!
      sparki.moveBackward(WALL_BACK); // move sparki backwards
      if (edge == RIGHT)
      {
        sparki.moveLeft(WALL_TURN);
      }
      else
      {
        sparki.moveRight(WALL_TURN);
      }
    }
  }
}

void loop() {

  //Scan for IR Receiver
  int code = sparki.readIR();

  // /------^-----\
  // |            |
  // | 69  70  71 |
  // | 68  64  67 |
  // |  7  21   9 |
  // | 22  25  13 |
  // | 12  24  94 |
  // |  8  28  90 |
  // | 66  82  74 |
  // \____________/

  switch(code){
    // Program Control
  case 64:  
    sparki.moveStop();
    sparki.RGB(0,0,0);
    program = false; 
    break;
  case 70:  
    program = true; 
    break;
  }  

  // Run Autonomy Code if
  if(program == true){

    sparki.RGB(RGB_GREEN);
    sparki.moveForward(); // move forward

      WallAvoidance();

    EdgeAvoidance();

    delay(100); // wait 0.1 seconds
  }
}

