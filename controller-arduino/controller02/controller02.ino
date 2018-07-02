int data[100];
int val2 = A0;
int val1 = A1;

void setup(){
  pinMode(val1, INPUT);
  pinMode(val2, INPUT);
  Serial.begin(9600);
}

void loop(){
 // individual channels of data transmitted, delya = 60 for 6 channels, f = 1/50
  while(1){
    data[0] = analogRead(val2);
    data[1] = analogRead(val1);
    data[2] = analogRead(A2);
    data[4] = analogRead(A3);
    data[5] = analogRead(A4);
    Serial.print(data[0]);
    Serial.print(":");
    Serial.print(data[1]);
    Serial.print(":");
    Serial.print(data[2]);
    Serial.print(":");
    Serial.print(data[3]);
    Serial.print(":");
    Serial.print(data[4]);
    Serial.print(":");
    Serial.print(data[5]);

    Serial.println();
    delay(1000);
  }

}
