#include <SPI.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include "DHT.h"
SoftwareSerial bluetooth(2, 3);

//GPIO ======================
int DHTPIN = 5;
int pressled = 8;
int gasled = 10;
int DHTled = 6;
int presspin = A4; 
int gaspin = A6;
int bigled = 9;
int cds = A5;
//====================== GPIO

//value ====================
float DHTs = 0;
int presss = 0;
int gass = 0;
float hic = 0;
int pressvalue = 0;
int gasvalue = 0;
//==================== value

void setup() {  
  Serial.begin(9600);
  
  pinMode(DHTled,OUTPUT);
  pinMode(gaspin,INPUT);
  pinMode(gasled,OUTPUT);
  pinMode(bigled,OUTPUT);

  setup_dht();
  setup_gas();
}

void loop() {    
  sensorSystem();
}

int sensorSystem()
{
  Serial.println(presss);
  Serial.println(gass);
  Serial.print("Heat index: ");
  Serial.print(DHTs);
  Serial.println(" *C ");
  
  // 위험 감지 시스템 시작
  int press1 = 500;
  int hic1 = 26;
  int gas1 = 500;
    
  if((presss >= press1) && (DHTs >= hic1) && (gass >= gas1)){
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,HIGH);
    Serial.println("A");
    bluetooth.println("A");
  }
  else if((presss >= press1) && (DHTs >= hic1) && (gass < gas1))
  {
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,LOW);
    Serial.println("B");
    bluetooth.println("B");
  }
  else if((presss >= press1) && (DHTs < hic1) && (gass >= gas1))
  {
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,HIGH);
    Serial.println("A");
    bluetooth.println("A");
  }
  
  else if((presss >= press1) && (DHTs < hic1) && (gass < gas1))
{
  digitalWrite(pressled,HIGH);
  digitalWrite(DHTled,LOW);
  digitalWrite(gasled,LOW);
    Serial.println("B");
  bluetooth.println("B");
    }
  else if((presss < press1) && (DHTs >= hic1) && (gass >= gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,HIGH);
    Serial.println("C");
    bluetooth.println("C");
    }
  else if((presss < press1) && (DHTs >= hic1) && (gass < gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,LOW);
    Serial.println("E");
    bluetooth.println("E");
  }
  else if((presss < press1) && (DHTs < hic1) && (gass >= gas1))
  { 
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,HIGH);
    Serial.println("C");
    bluetooth.println("C");
  }
  else if ((presss < press1) && (DHTs < hic1) && (gass < gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,LOW);
    Serial.println("E");
    bluetooth.println("E");
  }
  //  위험 감지 시스템 끝  
  delay(500);
  return 0;
}
