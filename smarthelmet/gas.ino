void setup_gas() {
}

void loop_gas() {
  int gasvalue = analogRead(gaspin);

  Serial.println(gasvalue);  
}
