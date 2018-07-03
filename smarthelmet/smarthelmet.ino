#include <SoftwareSerial.h>
#include <ArduinoJson.h>

//GPIO ======================
int nodeRx = 2;
int nodeTx = 3;

int DHTPIN = 5;

int pressled = 7;
int DHTled = 6;
int gasled = 10;

int bigled = 12;

int presspin = A1; 
int gaspin = A4;
int cds = A6;
//====================== GPIO

//value ====================
float hic = 0;
int presss = 0;
int gass = 0;
int pressvalue = 0;
//==================== value

//delaytime********************
int baudrate = 9600; 
unsigned int postdelaytime = 1000; // post to server delay time in ms
unsigned long actdiffTime = 0; // main scenario difference
unsigned long actprevTime = 0; // main scenario temp
unsigned long actdiffTime2 = 0; // main scenario difference
unsigned long actprevTime2 = 0; // main scenario temp
//********************delaytime 

SoftwareSerial nodemcuSerial(nodeRx, nodeTx); // RX, TX

void setup() {  
  Serial.begin(baudrate);
  nodemcuSerial.begin(9600);
  
  pinMode(DHTled,OUTPUT);
  pinMode(gasled,OUTPUT);
  pinMode(pressled,OUTPUT);
  pinMode(bigled,OUTPUT);
  pinMode(nodeTx,OUTPUT);

  setup_dht();
  setup_gas();
}

void loop() {    

  //for delay calculation*****************
  unsigned long currentTime = millis();
  actdiffTime = currentTime - actprevTime;
  //*****************for delay calculation

  if ( actdiffTime >= postdelaytime ){ // delaytime manage
    loop_dht();
    loop_cds();
    loop_gas();
    loop_pressure();
    actprevTime = currentTime;
  }  
    sensorSystem();
}

void sensorSystem(){

  unsigned long currentTime2 = millis();
  actdiffTime2 = currentTime2 - actprevTime2;
  
  // 위험 감지 시스템 시작
  int press1 = 500;
  int hic1 = 26;
  int gas1 = 500;
    
  if((presss >= press1) && (hic >= hic1) && (gass >= gas1)){
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,HIGH);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("TPG : High Stress & Pressure & Gas"); actprevTime2 = currentTime2;}
  }
  else if((presss >= press1) && (hic >= hic1) && (gass < gas1))
  {
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,LOW);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("TP : High Stress and Pressure"); actprevTime2 = currentTime2; }
  }
  else if((presss >= press1) && (hic < hic1) && (gass >= gas1))
  {
    digitalWrite(pressled,HIGH);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,HIGH);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("PG : High Pressure & Gas"); actprevTime2 = currentTime2;}
  }  
  else if((presss >= press1) && (hic < hic1) && (gass < gas1))
{
    digitalWrite(pressled,HIGH);  
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,LOW);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("P : High Pressure"); actprevTime2 = currentTime2;}
    }
  else if((presss < press1) && (hic >= hic1) && (gass >= gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,HIGH);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("TG : High Stress & Gas"); actprevTime2 = currentTime2;}
    }
  else if((presss < press1) && (hic >= hic1) && (gass < gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,HIGH);
    digitalWrite(gasled,LOW);
    if ( actdiffTime2 >= postdelaytime ) { Serial.println("TN : High Stress & Normal"); actprevTime2 = currentTime2;}
  }
  else if((presss < press1) && (hic < hic1) && (gass >= gas1))
  { 
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,HIGH);
     if ( actdiffTime2 >= postdelaytime ) { Serial.println("G : High Gas");actprevTime2 = currentTime2;}
  }
  else if ((presss < press1) && (hic < hic1) && (gass < gas1))
  {
    digitalWrite(pressled,LOW);
    digitalWrite(DHTled,LOW);
    digitalWrite(gasled,LOW);
     if ( actdiffTime2 >= postdelaytime ) { Serial.println("N : Normal");actprevTime2 = currentTime2;}
  }
  //  위험 감지 시스템 끝  

  
}

