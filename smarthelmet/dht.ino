#include <DHT.h>

//DHT******************** 
typedef enum
{
    DHTTYPE_DHT11         = DHT11, // DHT 11
    DHTTYPE_DHT22         = DHT22, // DHT 22, AM2302, AM2321
    DHTTYPE_DHT21         = DHT21 // DHT 21, AM2301
} DHTTYPE;

DHT dht(DHTPIN, DHTTYPE_DHT11);
float temp, humi;

void setup_dht(){
}

void loop_dht(){

  float h = dht.readHumidity();  
  float t = dht.readTemperature();
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
}

