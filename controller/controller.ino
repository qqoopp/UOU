#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiUdp.h>
#include <DHT.h>
#include<Wire.h>

//Device & Sensor info********************
const char* deviceno = "equip1";
const char* sensorno = "sensor1"; //dht
const char* sensorno2 = "sensor2"; //mpu
//********************Device & Sensor info

//GPIO******************** 
int pinDHT = D2;
int pinSCL = D6;
int pinSDA = D7;
//********************GPIO 

//updatetime********************
unsigned int updatetime_dht = millis(); // dht recent updatetime 
unsigned int updatetime_mpu = millis(); // mpu recent updatetime
unsigned int updatetime_ntp = millis(); // ntp recent updatetime
unsigned int updatetime_web = millis(); // web recent updatetime
//********************updatetime 

//delaytime********************
unsigned int postdelaytime = 5000;  // post to server delay time
unsigned int delaytime_dht = postdelaytime; //dht sensing time in msec
unsigned int delaytime_mpu = postdelaytime; //mpu sensing time in msec
unsigned int delaytime_ntp = postdelaytime; //ntp sensing time in msec
unsigned int delaytime_web = postdelaytime; //web sensing time in msec
//********************delaytime 

void setup(){
  Serial.begin(9600);  
  setup_ntp();  
  setup_dht();
  setup_mpu();
  setup_web();
}

void loop(){
  loop_ntp();
  loop_dht();
  loop_mpu(); 
  loop_web();
}

int isMeasure(unsigned int updatetime, unsigned int delaytime ){
  unsigned int currentTime = millis();  
  if ( currentTime - updatetime > delaytime ){
    return 1;
  }
  else {
    return 0;
  }
}

