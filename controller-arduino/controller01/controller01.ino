/*
Arduino to Raspberry pi with serial communication
transfer with json format
*/

#include <ArduinoJson.h>

const char ver[] = "0.1";
const char controllerid[] = "Arduino";
String sensors[] = {"DHT","MPU","SOUND"};

void setup(){
  Serial.begin(9600);
}

void loop(){

    for( int i=0; i<10; i++){
      if ( sensors[i] == NULL ) break;
      String sensor = sensors[i];
      sensor.toUpperCase();
      if ( sensor == "DHT") getDHT();
      if ( sensor == "MPU") getMPU();
      if ( sensor == "SOUND") getSOUND();
    }
    
    delay(3000);
}

void getDHT(){
    StaticJsonBuffer<200> jsonBuffer;
    JsonObject& root = jsonBuffer.createObject();

    root["controller"] = controllerid;        
    root["sensor"] = "DHT";
    root["time"] = 1351824120;
    root["temp"] = analogRead(A0);
    root["humi"] = analogRead(A1); 

    root.printTo(Serial);
    Serial.println("");
}

void getMPU(){
    StaticJsonBuffer<200> jsonBuffer;
    JsonObject& root = jsonBuffer.createObject();
    
    root["controller"] = controllerid;    
    root["sensor"] = "MPU";
    root["time"] = 1351824120;
    root["gyx"] = analogRead(A0);
    root["gyy"] = analogRead(A1); 
    root["gyz"] = analogRead(A2); 
    root["acx"] = analogRead(A3);
    root["acy"] = analogRead(A4); 
    root["acz"] = analogRead(A5); 

    root.printTo(Serial);
    Serial.println("");
}

void getSOUND(){
    StaticJsonBuffer<200> jsonBuffer;
    JsonObject& root = jsonBuffer.createObject();

    root["controller"] = controllerid;        
    root["sensor"] = "SOUND";
    root["time"] = 1351824120;
    root["decb"] = analogRead(A0); 

    root.printTo(Serial);
    Serial.println("");
}
