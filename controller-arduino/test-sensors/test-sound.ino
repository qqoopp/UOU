//Sound******************** 
int sound;
String jsonSOUND;
//********************Sound

void setup_sound(){
  
}

void loop_sound(){
  sound = analogRead(A0);

  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  
  root["controller"] = controllerid;        
  root["sensor"] = "SOUND";
  root["uptime"] = millis();
  root["decb"] = sound;

  //root.printTo(jsonSOUND);
  root.printTo(Serial);
  Serial.println("}");
}

