/**
  Project Embedded Systems
  Naam: Temperatuursensor
  Doel: Een temperatuursensor voor rolluiken, werkt zowel autonoom als via een centrale.

  @author Mark Dissel
  @version 7.2 08/11/2016
*/
#include <TM1638.h>
// Initialiseer de poorten
const int groeneLed = 2;
const int geleLed = 3;
const int rodeLed = 4;
const int autonoomLed = 5;
const int sensor = A0;
const int triggerPort = 6;
const int echoPort = 7;
const int datapin = 8;
const int strobepin = 9;
const int clockpin = 10;
const int knop1 = 11;
const int knop2 = 12;
const int knop3 = 13;
TM1638 module(datapin, clockpin, strobepin);

int knop1pressed = 0;
int knop2pressed = 0;
int knop3pressed = 0;

// Defineer vriabelen
int basisTemperatuur = 25;
int ingerold = 0;
int uitgerold = 0;
int afstand = 30;
int i = 0;
int tijdTemperatuur = 0;
int gemTemperatuur = 0;
int inofuitrollen = 0;
int metingen = 0;
int autonoom = 0;
int loopcounter = 0;
int knop2actief = 0;
int knop3actief = 0;
int moduleSet = 0;
int temperatuur = 0;
// Variabelen voor de Led&Key display
int buttons = 0;
int startValue = 0;
int buttonPressed = 1;
int dataOnScreen = 0;
int buttonChanged = 0;
int isError = 0;
int incOrDec = 0;
int incOrDecPressed = 0;
int autonoomPressed = 0;
int maxRoll = 50;

// Start initialisatie loop
void setup() {

  Serial.begin(9600);
  for (int pinNumber = 2; pinNumber < 6; pinNumber++) {
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
  pinMode( triggerPort, OUTPUT );
  pinMode( echoPort, INPUT );

  // Definieer de LED&KEY d.m.v. de import module

}

// Hier begint de loop
void loop() {
  sendCommand("baseTemperature", basisTemperatuur);
  sendCommand("rollStatus", ingerold ? 1 : (uitgerold ? 2 : 0)); // 0 in bezig, 1 = ingerold, 2 = uitgerold
  sendCommand("maxRoll", maxRoll);
  
  if (autonoom == 0) {
    digitalWrite(autonoomLed, HIGH);
  }
  else if (autonoom == 1) {
    digitalWrite(autonoomLed, LOW);
  }

  loopcounter++; //Count loops
  // Check of de knop1 ingedrukt wordt
  if (digitalRead(knop1) == 1 && inofuitrollen == 0) {
    if (!knop1pressed) {
      knop1pressed = 1;
      if (autonoom == 1) {
        autonoom = 0;
        knop2actief = 0;
        knop3actief = 0;

      } else if (autonoom == 0) {
        autonoom = 1;
      }
      sendCommand("autonoomPressed", autonoom);
    }
  } else {
    knop1pressed = 0;
  }
  //Check of de buttons op de Led&Key worden ingedrukt, zoja zet dit in een variabele
  if (module.getButtons() > 0 && module.getButtons() != buttonPressed) {
    module.clearDisplay();
    if (module.getButtons() == 64 && autonoom == 0) {
      basisTemperatuur--;
      
    }
    else if(module.getButtons() == 128 && autonoom == 0) {
      basisTemperatuur++;
      
    }
    else {
      buttonPressed = module.getButtons();
    }
  }
  // Hier wordt de naam van de data op het scherm getoond
  if (buttonPressed == 1) {
    String gemTemp = String(gemTemperatuur);
    module.setDisplayToString("GEMI " + gemTemp);
  }
  if (buttonPressed == 2) {
    if (isError == 1) {
      module.clearDisplay();
      module.setDisplayToString("ERROR");
    }
    else if (isError == 0) {
      String distance = String(afstand);
      module.setDisplayToString("AFST " + distance);
    }
  }
  if (buttonPressed == 4) {
    String basis = String(basisTemperatuur);
    module.setDisplayToString("BASI " + basis);
  }
  if (buttonPressed == 8) {
    if (ingerold == 1) {
      module.clearDisplay();
      module.setDisplayToString("INGEROLD");
    }
    else if (uitgerold == 1) {
      module.clearDisplay();
      module.setDisplayToString("UITGEROLD");
    }
    else if (inofuitrollen == 1) {
      module.clearDisplay();
      module.setDisplayToString("BEZIG");
    }
    else {
      module.clearDisplay();
      module.setDisplayToString("METEN");
    }
  }
  
  //Input
  if (digitalRead(knop2) == 1 && autonoom == 1 && inofuitrollen == 0) {
    if (!knop2pressed) {
      knop2pressed = 1;
      knop2actief = 1;
      knop3actief = 0;
    }
  } else {
    knop2pressed = 0;
  }
  if (digitalRead(knop3) == 1 && autonoom == 1 && inofuitrollen == 0) {
    if (!knop3pressed) {
      knop3pressed = 1;
      knop2actief = 0;
      knop3actief = 1;
    }
  } else {
    knop3pressed = 0;
  }

  if (knop2actief == 1 && ingerold != 1 ) {
    inrollen();
  }
  else if (knop3actief == 1 && uitgerold != 1) {
    uitrollen();
  }
  if (loopcounter % 10 == 1) { //Every 1s
    berekenAfstand();
  }

  if (autonoom == 0) {
    int sensorWaarde = analogRead(sensor);
    float voltage = (sensorWaarde / 1024.0) * 5;
    temperatuur = ((voltage * 1000) - 500) / 10;

    i++;
    tijdTemperatuur += temperatuur;
    if (i == 10) {
      gemTemperatuur = (tijdTemperatuur / 10);
      tijdTemperatuur = 0;
      i = 0;
      sendCommand("temperature", gemTemperatuur);
    }
    // Als de gemiddelde temperatuur hoog ligt, wordt er uitgerold.
    if (gemTemperatuur > basisTemperatuur && uitgerold == 0 && gemTemperatuur != 0) {
      uitrollen();
    }

    // Als de gemiddelde temperatuur laag ligt, wordt er ingerold.
    if (gemTemperatuur <= basisTemperatuur && ingerold == 0 && gemTemperatuur != 0) {
      inrollen();
    }
  }



  if (ingerold == 1) {
    digitalWrite(groeneLed, HIGH);
    digitalWrite(geleLed, LOW);
  }
  else if (uitgerold == 1) {
    digitalWrite(rodeLed, HIGH);
    digitalWrite(geleLed, LOW);
  }

  if (inofuitrollen == 1) {
    delay (50);
  }
  else {
    delay(100);
  }
}

void berekenAfstand() {
  digitalWrite(triggerPort, LOW);      // Trigger output op 0 zetten.
  digitalWrite(triggerPort, HIGH);    // Stuur nu een signaal van 10 ms naar de triggerport.
  delayMicroseconds( 10 );
  digitalWrite(triggerPort, LOW);  // zet de triggerpoort weer op 0.

  int duration = pulseIn(echoPort, HIGH); // Sla de duur van de afstand op in variabele duration

  afstand = 0.034 * duration / 2;  // Snelheid geluid = 340 m/s en 0.034 cm/us, en delen door twee, doordat de afstand twee keer overbrugd wordt.
  if (afstand < 0) {
    afstand = 0;
  }
  if (afstand == 0) {
    isError = 1;
  }
  if (afstand > 0) {
    isError = 0;
  }
}


void inrollen() {
  uitgerold = 0;
  inofuitrollen = 1;
  digitalWrite(rodeLed, LOW);
  digitalWrite(groeneLed, HIGH);
  digitalWrite(geleLed, HIGH);
  delay(50);
  digitalWrite(geleLed, LOW);
  if (afstand > maxRoll && afstand != 0) {
    ingerold = 1;
    inofuitrollen = 0;
  }
}

void uitrollen() {
  inofuitrollen = 1;
  ingerold = 0;
  digitalWrite(groeneLed, LOW);
  digitalWrite(rodeLed, HIGH);
  digitalWrite(geleLed, HIGH);
  delay(50);
  digitalWrite(geleLed, LOW);
  if (afstand < 5 && afstand != 0) {
    uitgerold = 1;
    inofuitrollen = 0;
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
  if(command == "incBase") {
    basisTemperatuur++;
  }
  if(command == "decBase") {
    basisTemperatuur--;
  }
  if(command == "incMaxRoll") {
    maxRoll++;
  }
  if(command == "decMaxRoll") {
    maxRoll--;
  }
  if(command == "rollIn") {
    if(uitgerold == 1) {
      inrollen();
    }
  }
  if(command == "rollOut") {
    if(ingerold == 1) {
      uitrollen();
    }
  }
  if(command == "autonoom") {
    if(inofuitrollen == 0) {
      autonoom = data;
      sendCommand("autonoomPressed", autonoom);
    }
  }
}

