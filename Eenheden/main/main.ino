
void setup(void) {
  Serial.begin(9600);   
}

int total = 0;

void writeSerial(String str) {
  Serial.write(str.length());
  Serial.print(str);
}

void loop(void) {
  total++;
  writeSerial("hello" + String(total));
  
  delay(1000);
}

