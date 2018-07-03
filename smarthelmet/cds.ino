void loop_cds(){
  
  int cdss = analogRead(cds);
  Serial.print("cds =  ");
  Serial.println(cdss);

  if (cdss > 750) {
    digitalWrite(bigled, HIGH);
    Serial.println("LED ON ");
  }
  else {
    digitalWrite(bigled, LOW);
    Serial.println("LED OFF ");
  }  

}

