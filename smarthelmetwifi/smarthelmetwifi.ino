#include <SoftwareSerial.h>

//GPIO ======================
int nodeRx = 3;
int nodeTx = 2;
//====================== GPIO

//delaytime********************
int baudrate = 9600; 
unsigned int postdelaytime = 1000; // post to server delay time in ms
unsigned long actdiffTime = 0; // main scenario difference
unsigned long actprevTime = 0; // main scenario temp
unsigned long actdiffTime2 = 0; // main scenario difference
unsigned long actprevTime2 = 0; // main scenario temp
//********************delaytime 

SoftwareSerial nodemcuSerial(nodeRx, nodeTx); // RX, TX
String TagData;

void setup() {  
  Serial.begin(baudrate);
  nodemcuSerial.begin(9600);
  pinMode(nodeRx,OUTPUT);
}

void loop() {    
  while(nodemcuSerial.available() > 0) 
      {
        
          byte incomingData = nodemcuSerial.read();
          TagData = TagData + String(incomingData);
          Serial.println(TagData);
      }


}

