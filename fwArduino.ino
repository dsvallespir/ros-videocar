#include <Servo.h>

#define FRAME_INIT 1
#define FRAME_DATA 2
#define FRAME_END 3

#define MIN_SERVO_VAL 30
#define MAX_SERVO_VAL 90

byte recv;
byte stateFrame = FRAME_INIT;
int i;
byte buff[5];


int ENA = 5;                        //L298使能A
int ENB = 6;                        //L298使能B
int INPUT2 = 7;                     //电机接口1
int INPUT1 = 8;                     //电机接口2
int INPUT3 = 12;                    //电机接口3
int INPUT4 = 13;                    //电机接口4
Servo servo1;                       // 创建舵机#1号
Servo servo2;                       // 创建舵机#2号
Servo servo3;                       // 创建舵机#3号
Servo servo4;                       // 创建舵机#4号
//Servo servo5;                      // 创建舵机#5号
//Servo servo6;                      // 创建舵机#6号
Servo servo7;                       // 创建舵机#7号
Servo servo8;                       // 创建舵机#8号  


  int servo1_value = 90;
  int servo2_value = 90;

#define MOTOR_GO_FORWARD  {digitalWrite(INPUT1,LOW);digitalWrite(INPUT2,HIGH);digitalWrite(INPUT3,LOW);digitalWrite(INPUT4,HIGH); delay(100);}    //车体前进                          
#define MOTOR_GO_BACK      {digitalWrite(INPUT1,HIGH);digitalWrite(INPUT2,LOW);digitalWrite(INPUT3,HIGH);digitalWrite(INPUT4,LOW);delay(100);}   //车体后退
#define MOTOR_GO_RIGHT    {digitalWrite(INPUT1,HIGH);digitalWrite(INPUT2,LOW);digitalWrite(INPUT3,LOW);digitalWrite(INPUT4,HIGH);delay(100);}    //车体右转
#define MOTOR_GO_LEFT     {digitalWrite(INPUT1,LOW);digitalWrite(INPUT2,HIGH);digitalWrite(INPUT3,HIGH);digitalWrite(INPUT4,LOW);delay(100);}    //车体左转
#define MOTOR_GO_STOP     {digitalWrite(INPUT1,LOW);digitalWrite(INPUT2,LOW);digitalWrite(INPUT3,LOW);digitalWrite(INPUT4,LOW);delay(100);}      //车体停止



void setup() {
  // put your setup code here, to run once:
  
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(INPUT1, OUTPUT);
  pinMode(INPUT2, OUTPUT);
  pinMode(INPUT3, OUTPUT);
  pinMode(INPUT4, OUTPUT);

  digitalWrite(ENA, HIGH);
  digitalWrite(ENB, HIGH);


  //servo1.attach(3);                       //定义舵机1控制口
  //servo2.attach(4);                       //定义舵机2控制口
  servo3.attach(2);                       //定义舵机3控制口
  servo4.attach(11);                      //定义舵机4控制口
  servo1.attach(9);                       //定义舵机7控制口
  servo2.attach(10);                      //定义舵机8控制口


  Serial.begin(9600);
  while(!Serial){ 
    ;
  }
  
  Serial.println("Smart Car iniciado");

  //MOTOR_GO_FORWARD;
  //delay(100);
  //MOTOR_GO_STOP;

  servo1.write(servo1_value);
  servo2.write(servo2_value);

  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()){
    recv = Serial.read();

    switch(stateFrame){
      case FRAME_INIT:{ 
        if(recv == '#'){
          stateFrame = FRAME_DATA;
          i = 0;
        }
       break;
      case FRAME_DATA:{
        if(i < 3){
          buff[i] = recv;
          i++;
        }
        if(i == 3){
          stateFrame = FRAME_END;
        }
        break;
      }
      case FRAME_END:{
        if(recv == '$'){
          Serial.println("Trama recibida correctamente");
          stateFrame = FRAME_INIT;
          
          if(buff[0] == '0'){
            switch(buff[1]){
              case '1': { 
                MOTOR_GO_FORWARD; 
                Serial.println("MOTOR_GO_FORWARD"); 
                break;
              }
              case '2':{
                MOTOR_GO_BACK;    
                Serial.println("MOTOR_GO_BACK"); 
                break;
                }
              case '3':{
                MOTOR_GO_LEFT;    
                Serial.println("MOTOR_GO_LEFT"); 
                break;
                }
              case '4':{
                MOTOR_GO_RIGHT;   
                Serial.println("MOTOR_GO_RIGHT"); 
                break;
                }
              case '0':{
                MOTOR_GO_STOP;    
                Serial.println("MOTOR_GO_STOP"); 
                break;
                }
              case '5':{
                if (buff[2] == 'Z'){
                  //pantitl up
                  if(servo1_value >= MIN_SERVO_VAL && servo1_value <= MAX_SERVO_VAL){
                    servo1_value += SERVO_STEP_VAL;
                    servo1.write(servo1_value);
                  }
                }
                if (buff[2] == '%'){
                  //pantitl down
                  if(servo1_value >= MIN_SERVO_VAL && servo1_value <= MAX_SERVO_VAL){
                    servo1_value -= SERVO_STEP_VAL;
                    servo1.write(servo1_value);
                  }
                }
                break;
              }
              case '6':{
                if (buff[2] == 'Z'){
                  //pantitl left
                  if(servo2_value >= MIN_SERVO_VAL && servo2_value <= MAX_SERVO_VAL){
                    servo2_value += SERVO_STEP_VAL;
                    servo2.write(servo2_value);
                  }
                }
                if (buff[2] == '%'){
                  //pantitl right
                  if(servo2_value >= MIN_SERVO_VAL && servo2_value <= MAX_SERVO_VAL){
                    servo2_value -= SERVO_STEP_VAL;
                    servo2.write(servo2_value);
                  }
                }
              break;
              }
              default:{
                Serial.println("Error en la recepción del comando");
                break; 
              }
                
            }
          }
        }
      break;
      }
      default:{
        Serial.println("Error en la recepción de la trama");
        break;
      }
    }
  }
 }
}
