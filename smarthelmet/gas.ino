void setup_gas() {
}

void loop_gas() {
  gass = analogRead(gaspin);
  Serial.print("Gas : ");
  Serial.println(gass);  

  //Json data generation ============================
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();

  root["measuredt"] = "";       
  root["controller"] = "smarthelmet";        
  root["sensor"] = "GAS";
  root["uptime"] = millis();
  root["gas"] = gass;
  
  //root.printTo(jsonResult);
  root.printTo(Serial);
  Serial.println("");
  //============================Json data generation
}
