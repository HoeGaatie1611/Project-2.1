
void setup(void) {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

int total = 0;

void loop(void) {
  delay(1000);
  total++;
  sendCommand("testCommand", total);

  if(total % 2 == 0) {
    //digitalWrite(13, HIGH);
  } else {
    //digitalWrite(13, LOW);
  }
}

void sendCommand(String command, int data) {
  String commandString = command + " " + data;
  
  Serial.write(commandString.length());
  Serial.print(commandString);
}

void serialEvent() {
  String command = "";
  bool commandDone = false;
  String dataString = "";
  
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    
    if((String) inChar == " ") {
      commandDone = true;
      continue;
    }
    if(!commandDone) {
      command += inChar;
    } else {
      dataString += inChar;
    }
  }

  processCommand(command, dataString.toInt());
}

void processCommand(String command, int data) {
  if(command == "ledOn") {
    digitalWrite(data, HIGH);
  }
  if(command == "ledOff") {
    digitalWrite(data, LOW);
  }
}
