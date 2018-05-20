//Host Server config********************
const char* ssid     = "Public WiFi@Seoul2";
const char* password = "11112222";
const char * host = "192.168.10.12"; // ip or dns
const uint16_t port = 8000;
IPAddress myIP;
//********************Host Server config

void setup_web(){
    //IPAddress zeroip;
    //WiFi.config(zeroip, zeroip, zeroip); 
    //delay(100);
    WiFi.mode(WIFI_STA);
    delay(100);
    WiFi.begin( ssid, password );

    Serial.println();
    Serial.println();
    Serial.print("Wait for WiFi... ");

    while(WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }

    myIP = WiFi.localIP();

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.print("IP address: ");
    Serial.println(myIP);
    delay(10);
}

void loop_web(){

    if ( !isMeasure(updatetime_web, delaytime_web) ){
      return;
    }
    updatetime_web = millis();

    Serial.print(myIP);
    Serial.print(" --> ");
    Serial.println(host);

    if(WiFi.status() == WL_CONNECTED) {
      post_json_dht();
      post_json_mpu();
    }

    Serial.print("wait ");
    Serial.print(String(postdelaytime));
    Serial.println(" sec...");
}

void post_json_dht(){
  String postdata = "";
  postdata += "{\"data\":[";
  postdata += "{\"hm\":\"" + String(hm) + "\","; 
  postdata += "\"equipno\":\"" + String(deviceno) + "\","; 
  postdata += "\"sensorno\":\"" + String(sensorno) + "\",";   
  postdata += "\"value\":"; 
  postdata += "{\"temp\":" + String(temp) + ",";
  postdata += "\"humi\":" + String(humi) + "}"; 
  postdata += "}]}"; 
  sendhttp(postdata);
}

void post_json_mpu(){
  String hosturl = "http://" + String(host) + ":" + String(port) + "/PostMeasure";
  String postdata = "";
  postdata += "{\"data\":[";
  postdata += "{\"hm\":\"" + String(hm) + "\","; 
  postdata += "\"equipno\":\"" + String(deviceno) + "\","; 
  postdata += "\"sensorno\":\"" + String(sensorno2) + "\",";   
  postdata += "\"value\":"; 
  postdata += "{\"acx\":" + String(acx) + ",";
  postdata += "\"acy\":" + String(acy) + ",";
  postdata += "\"acz\":" + String(acz) + ","; 
  postdata += "\"gyx\":" + String(gyx) + ",";
  postdata += "\"gyy\":" + String(gyy) + ","; 
  postdata += "\"gyz\":" + String(gyz) + "}"; 
  postdata += "}]}"; 
  sendhttp(postdata);
}

void sendhttp(String postdata){ 
  String hosturl = "http://" + String(host) + ":" + String(port) + "/PostMeasure";
  
  HTTPClient http;
  http.begin(hosturl);
  //http.addHeader("POST /PostMeasure HTTP/1.1");
  http.addHeader("Content-Type", "application/json");
  http.addHeader("Cache-Control","no-cache");
  http.POST(postdata);
  http.writeToStream(&Serial);
  String rtnmsg = http.getString();
  http.end();

  //Serial.println(rtnmsg);
  Serial.println("posted");
}

