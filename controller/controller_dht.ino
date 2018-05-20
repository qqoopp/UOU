//DHT******************** 
typedef enum
{
    DHTTYPE_DHT11         = DHT11, // DHT 11
    DHTTYPE_DHT22         = DHT22, // DHT 22, AM2302, AM2321
    DHTTYPE_DHT21         = DHT21 // DHT 21, AM2301
} DHTTYPE;

DHT dht(pinDHT, DHTTYPE_DHT11);
float temp, humi;
String strValue;
//********************DHT 

void setup_dht(){
  dht.begin();
  updatetime_dht = millis();  
}

void loop_dht(){

  if ( !isMeasure(updatetime_dht, delaytime_dht) ){
    return;
  }
  updatetime_dht = millis();
  temp = dht.readTemperature();
  humi = dht.readHumidity();
  
  if ( !isFloat(String(temp)) ) { 
    temp = 0;
    humi = 0;
  }
}

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
