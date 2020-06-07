#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo s;
int pos1 = 0;
int pos = 0;
void initialize_motor()
{
  s.
  write(0);
  delay(100);
  s.write(100);
  delay(100);
  Serial.println("motor is ready");
}

void setup() {
  myservo1.attach(9);
  myservo2.attach(11);
  s.attach(6);
  Serial.begin(115200);
  initialize_motor();
}
//ANGLE RANGE IS 0 TO 110
//ANGLE FOR BREAK 0 FOR BREAK CONDITION AND 70 FOR NON BREAK
int i = 55; // TAKE THE CURRNET ANGEL OF SERVO-1

int Start = 0;
int Break;
String Sign_angle;
int Angle;
String Sign_speed;
int serial_speed = 1550;
int speed_motor = 1550;
String instring = "";

// 1430*speed forward
// 1730 *speed forward
void loop()
{

  Serial.println(instring);
  if (instring.length() != 10)
    return;
  Start = instring.substring(0, 1).toInt();
  Break = instring.substring(1, 2).toInt();
  Sign_angle = instring.substring(2, 3);
  Angle = instring.substring(3, 6).toInt();
  Sign_speed = instring.substring(6, 7);
  serial_speed = instring.substring(7, 10).toInt();

  if (Sign_angle == "-")
  {
    Angle = Angle * (-1);
  }
  if (Sign_speed == "-")
  {
    serial_speed = map(serial_speed, 0, 255, 1550, 1430);
  }
  else
    serial_speed = map(serial_speed, 0, 255, 1580, 1730);
  Serial.println(instring);
  //initially 0 and 110
  pos1 = map(Angle, -254, 254, 20, 90 );
  int j = 0;

  if (Start == 1)
  {
    //Serial.println("fsf");
    myservo1.write(pos1);

    if (Break == 1)
    {
      speed_motor = 1550;
      //////////////////first down the speed and then applied break
      if (serial_speed < speed_motor)
      {
        for (; speed_motor > serial_speed; speed_motor = speed_motor - 5)
        {

          s.writeMicroseconds(speed_motor);
          delay(1);
        }
        Serial.println(speed_motor);
      }
      else if (serial_speed > speed_motor)
      {
        for (; speed_motor < serial_speed; speed_motor = speed_motor + 5)
        {

          s.writeMicroseconds(speed_motor);
          delay(1);
        }
        Serial.println(speed_motor);
      }
      //////////////////////////
      myservo2.write(10);
      serial_speed = 1550;

    }
    else
    {
      myservo2.write(70);
    }

    if (serial_speed < speed_motor)
    {
      for (; speed_motor > serial_speed; speed_motor = speed_motor - 5)
      {

        s.writeMicroseconds(speed_motor);
        //delay(1);
      }
      Serial.println(speed_motor);
    }
    else if (serial_speed > speed_motor)
    {
      for (; speed_motor < serial_speed; speed_motor = speed_motor + 5)
      {

        s.writeMicroseconds(speed_motor);
        //delay(1);
      }
      Serial.println(speed_motor);
    }

  }

}

void serialEvent() {
  instring = Serial.readStringUntil('\n');
}
