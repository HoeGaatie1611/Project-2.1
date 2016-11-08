
void setup(void) {
  Serial.begin(9600);   
}

int total = 0;

void sendCommand(String command, int data) {
  String commandString = command + " " + data;
  
  Serial.write(commandString.length());
  Serial.print(commandString);
}

void loop(void) {
  total++;
  sendCommand("testCommand", total);
  
  delay(10000);
}

