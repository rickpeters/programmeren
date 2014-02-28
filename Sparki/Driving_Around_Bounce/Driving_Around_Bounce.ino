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
  sparki.clearLCD(); // clear the LCD
}

// constants and initialization
const int NONE  = 0;
const int LEFT  = 1;
const int RIGHT = 2;
const int WALL_TURN = 45;
const int WALL_BACK = 3;
const int EDGE_TURN = 20;
const int EDGE_BACK = 2;
int edge = NONE;
int program = false;

// helper functions
void EdgeAvoidance() {
  int angle = 0; // the angle at which the edge is reached
  // edge avoidance
  int edgeLeft   = sparki.edgeLeft();   // measure the left edge IR sensor
  int edgeRight  = sparki.edgeRight();  // measure the right edge IR sensor

  int threshold = 200; // if below this value, no surface underneath

  if (edgeLeft < threshold) // if no surface underneath left sensor
  {
    edge = LEFT;
    sparki.RGB(RGB_BLUE); // turn the led blue
    // stop sparki
    sparki.moveStop();
    angle = EdgeAngle(edge);
    // and now we should bounce against the edge and turn
	sparki.moveRight(angle);
  }

  if (edgeRight < threshold) // if no surface underneath right sensor
  {
    edge = RIGHT;
    sparki.RGB(RGB_BLUE); // turn the led blue
    // stop sparki
    sparki.moveStop();
    angle = EdgeAngle(edge);
    // and now we should bounce against the edge and turn
	sparki.moveLeft(angle);
  }
}

int EdgeAngle(int edge) {
	// this function determines the angle at which the edge is reached
	// it does this by slowly advancing and measuring when the second
	// sensor reaches the edge. By using pythagoras's theorem the angle
	// can be calculated
	// precondition: sparki has reached full stop and parameter edge
	// contains LEFT or RIGHT depending on the sensor that is already
	// over the edge
	int threshold = 200; // if below this value, no surface underneath
	float distance = 0;
	float step = 0.2; // stepsize for moving over the edge
    float heading = 0; // in which heading is edge reached
	
	if (edge == LEFT)
	{
		int edgeRight = sparki.edgeRight();
		while (edgeRight > threshold )
		{
			distance += step;
			sparki.moveForward(step);
			edgeRight = sparki.edgeRight();
		}
		sparki.print("Distance : ");
		sparki.println(distance);
                sparki.updateLCD();
		// backup, to prevent falling
		sparki.moveBackward(distance);
	}
	else if (edge == RIGHT)
	{
		int edgeLeft = sparki.edgeLeft();
		while (edgeLeft > threshold )
		{
			distance += step;
			sparki.moveForward(step);
			edgeLeft = sparki.edgeLeft();
		}
		sparki.print("Distance : ");
                sparki.updateLCD();
		sparki.println(distance);
		// backup, to prevent falling
		sparki.moveBackward(distance);
	}
	else
	{
		// error
		sparki.println("Error!");
	}
	// now we have to calculate the angle
	const float sensorwidth = 8; // distance between edge sensors
	heading = 180 * atan2(sensorwidth, distance) / PI;
    sparki.print("Heading : ");
    sparki.println(heading);
    sparki.updateLCD();
    delay(10000);
    return heading;
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
    
    sparki.updateLCD();

    delay(100); // wait 0.1 seconds
  }
}

