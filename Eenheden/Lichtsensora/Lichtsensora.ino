int photocellPin = A0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider
int remand = 0;
 
void setup(void) {
  Serial.begin(9600);   
}
 
void loop(void) {
  photocellReading = analogRead(photocellPin);  
 
  Serial.print("Analog reading = ");
  Serial.print(photocellReading);     // the raw analog reading
 
  // We'll have a few threshholds, qualitatively determined
 // if (photocellReading < 10) {
 //   Serial.println(" - Dark");
// } else if (photocellReading < 200) {
 //   Serial.println(" - Dim");
// } else if (photocellReading < 500) {
 //   Serial.println(" - Light");
 // } else if (photocellReading < 800) {
 //   Serial.println(" - Bright");
 // } else {
 //   Serial.println(" - Very bright");
//  }
  Serial.println("Remand waarde: ");
  remand = photocellReading/5;
  Serial.println(remand);
  
  delay(3000);    // 1 sec delay
}


//ok
