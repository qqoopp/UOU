void loop_pressure(){
  presss = analogRead(presspin);
  Serial.print("Pressure : ");
  Serial.println(presss);  
  
  //Json data generation ============================
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();

  root["measuredt"] = "";       
  root["controller"] = "smarthelmet";        
  root["sensor"] = "PRESSURE";
  root["uptime"] = millis();
  root["pressure"] = presss;
  
  //root.printTo(jsonResult);
  root.printTo(Serial);
  Serial.println("");
  //============================Json data generation
}

