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

// set these constants to 1 once Angles and Distances are 1 to 1
//const float ANGLE_ADJUST =  1.9584;
const float ANGLE_ADJUST =  1.0;
//const float DISTANCE_ADJUST = 1.9584;
const float DISTANCE_ADJUST = 1.1;
const int SEARCH_DISTANCE = 30; // 30 cm radius
bool doMove = false;

void setup()
{       
  sparki.servo(SERVO_CENTER); // center the servo
  // open gripper
  sparki.gripperOpen();
  delay(5000);
  sparki.gripperStop();
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

void findLoop()
{
  sparki.clearLCD(); 
  
  if(turnToTarget())
  {   
      delay(500);  // these delays seem to improve ping response - not sure why
    
    int moveDistance= sparki.ping();        
    // move closer target if more than 10cm away, we'll scan again and adjust angle
    if(moveDistance>10)
    {      
      delay(500);
      moveToTarget(0.50);
      // adjust postion to point at target again
      delay(500);
      turnToTarget();
    }  
    delay(500);
    // move to target now
    moveToTarget(1);

    // close gripper
    sparki.gripperClose();
    delay(4000);
    sparki.gripperStop();
    
    goRandomAndDrop();
    
    
  }
  else    
  {
    // didn't find anything
    if(doMove)
    {
      // either move in a random direction
      goRandom();
    }
    else    
    {
      // or turn around
      sparki.moveRight(180 * ANGLE_ADJUST);
    }
    
    // next time we don't find anything try doing something different
    doMove = !doMove;
    
  }
  sparki.updateLCD();
  delay(5000); // wait 5 seconds
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
    findLoop();
  }
}

// move to target directly ahead, can pass adjustment so only move 50% of distance or 100% etc.
void moveToTarget(float adjustment)
{
    // get distance
    int moveDistance= sparki.ping();        
    if(moveDistance<SEARCH_DISTANCE)
    {
      sparki.moveForward(moveDistance * adjustment * DISTANCE_ADJUST);
    }

}


// find the closest target and turn towards it
bool turnToTarget()
{
  int targetAngle = FindTarget();
    
  if(targetAngle>-180)
  {
    if(targetAngle<0)
    {
     sparki.moveLeft((targetAngle*-1) * ANGLE_ADJUST);
    }
    if(targetAngle>0)
    {
      sparki.moveRight(targetAngle * ANGLE_ADJUST);
    }
    
    // look at object - should be straight ahead now
    sparki.servo(SERVO_CENTER);
    sparki.RGB(RGB_GREEN);
    return true;
  }
  
  return false;
}


// move in a random direction
void goRandom()
{
  float step = 0.2;
  int angle = random(0,360);
  int distance = random(5,50);
  
  sparki.moveRight(angle * ANGLE_ADJUST);
  // create a loop to move a certain distance and prevent falling off
  // the edge
  for (traveled = 0; traveled <= distance; traveled += step)
  {
    sparki.moveForward(step);
    edgeAvoidance();
  }
  
}

// go somewhere random, drop whatever is being held
// then return to original position
void goRandomAndDrop()
{
  int angle = random(0,360);
  int distance = random(10,30);
  
  sparki.moveRight(angle * ANGLE_ADJUST);
  sparki.moveForward(distance * DISTANCE_ADJUST);
  
    // open gripper
    sparki.gripperOpen();
    delay(8000);
    sparki.gripperStop();
    sparki.RGB(0,0,0);

  sparki.moveBackward(distance * DISTANCE_ADJUST);
  sparki.moveLeft(angle * ANGLE_ADJUST);
 
}

// find target - will return angle of found target (or -180 if nothing found)
int FindTarget()
{
   int closest = SEARCH_DISTANCE;  // nothing more the xCM away
   int angle = -180;
  
    // look around and find an object
    for(int servoAngle = -90; servoAngle<=90; servoAngle+=5)
    {
      sparki.servo(servoAngle);
      int distance = sparki.ping();
      
      if(distance!=-1 && distance<closest)
      {
        sparki.beep(); // Sparki beeps!        
        
        angle = servoAngle;
        closest = distance;
      }
    } 

  if(angle!=-180)
  {
    // got a rough target - do a finer search
    for(int servoAngle = max(-90,angle - 10); servoAngle<=min(90,angle + 10); servoAngle+=1)
    {
      sparki.servo(servoAngle);
      int distance = sparki.ping();
      
      if(distance!=-1 && distance<closest)
      {
        angle = servoAngle;
        closest = distance;
      }
    } 
    
    // look at target
    sparki.servo(angle);
  }
  else
  {
    // didn't find anything
    sparki.servo(SERVO_CENTER);
  }
  

   return angle;      
}
