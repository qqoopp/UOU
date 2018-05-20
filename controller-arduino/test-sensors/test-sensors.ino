#include <DHT.h>
#include<Wire.h>
#include <ArduinoJson.h>

//Device & Sensor info********************
const char ver[] = "v0.1";  //version info for source management
const char controllerid[] = "Arduino"; //controller id
String sensors[] = {"DHT","MPU","SOUND"};//connected sensors
//********************Device & Sensor info

//GPIO******************** 
int pinDHT = 3;
int pinSCL = A5;
int pinSDA = A4;
int pinSound = A0;
//********************GPIO 

//delaytime********************
unsigned int postdelaytime = 1;  // post to server delay time in ms
//********************delaytime 

void setup(){
  Serial.begin(2000000);  
  
  for( int i=0; i<10; i++){
      if ( sensors[i] == NULL ) break;
      String sensor = sensors[i];
      sensor.toUpperCase();
      if ( sensor == "DHT") setup_dht();
      if ( sensor == "MPU") setup_mpu();
      if ( sensor == "SOUND") setup_sound();
   }
}

void loop(){

   for( int i=0; i<10; i++){
      if ( sensors[i] == NULL ) break;
      String sensor = sensors[i];
      sensor.toUpperCase();
      if ( sensor == "DHT") loop_dht();
      if ( sensor == "MPU") loop_mpu();
      if ( sensor == "SOUND") loop_sound();
   }

  delay(postdelaytime); //delay
}

// check whether data is numeric
boolean isFloat(String tString) {
  String tBuf;
  boolean decPt = false;
  
  if(tString.charAt(0) == '+' || tString.charAt(0) == '-') tBuf = &tString[1];
  else tBuf = tString;  

  for(int x=0;x<tBuf.length();x++)
  {
    if(tBuf.charAt(x) == '.') {
      if(decPt) return false;
      else decPt = true;  
    }    
    else if(tBuf.charAt(x) < '0' || tBuf.charAt(x) > '9') return false;
  }
  return true;
}

