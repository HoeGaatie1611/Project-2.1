/**
  Project Embedded Systems
  Naam: Remandsensor
  Doel: Een Remandsensor voor rolluiken, werkt zowel autonoom als via een centrale.

  @author Dennis Vrieling & Remand Knol
  @version 6.2 08/11/2016
*/
#include <TM1638.h>
// Initialiseer de poorten
const int groeneLed = 2;
const int geleLed = 3;
const int rodeLed = 4;
const int autonoomLed = 5;
const int sensor = A0;
const int triggerPort = 8;
const int echoPort = 7;
const int knop1 = 9;
const int knop2 = 10;
const int knop3 = 11;
const int strobepin = 6;
const int clockpin = 12;
const int datapin = 13;
int Remand = 0;
int sensormeten;
TM1638 module(datapin, clockpin, strobepin);

int knop1pressed = 0;
int knop2pressed = 0;
int knop3pressed = 0;

// Defineer vriabelen
const int basisRemand = 50;
int ingerold = 0;
int uitgerold = 0;
int afstand = 30;
int i = 0;
int tijdRemand = 0;
int gemRemand = 0;
int inofuitrollen = 0;
int metingen = 0;
int autonoom = 0;
int loopcounter = 0;
int knop2actief = 0;
int knop3actief = 0;
int moduleSet = 0;

// Start initialisatie loop
void setup() {
  Serial.begin(9600);
  for(int pinNumber = 2; pinNumber < 6; pinNumber++) {
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
  pinMode( triggerPort, OUTPUT );
  pinMode( echoPort, INPUT );
}

// Hier begint de loop 
void loop() {
  if(autonoom == 0) {
    digitalWrite(autonoomLed, HIGH);
  }
  else if(autonoom == 1) {
    digitalWrite(autonoomLed, LOW);
  }
  
  loopcounter++; //Count loops
    if(digitalRead(knop1) == 1 && inofuitrollen == 0) {
    if(!knop1pressed) {
     knop1pressed = 1;
     if(autonoom == 1) {
        autonoom = 0;
        knop2actief = 0;
        knop3actief = 0;
        
    } else if(autonoom == 0) {
        autonoom = 1;
    }
      sendCommand("autonoomPressed", autonoom);
    }
  } else {
    knop1pressed = 0;
  }
  //Input
  if(digitalRead(knop2) == 1 && autonoom == 1 && inofuitrollen == 0) {
    if(!knop2pressed) {
      knop2pressed = 1;
      knop2actief = 1;
      knop3actief = 0;
    }
  } else {
    knop2pressed = 0;
  }
  if(digitalRead(knop3) == 1 && autonoom == 1 && inofuitrollen == 0) {
    if(!knop3pressed) {
      knop3pressed = 1;
      knop2actief = 0;
      knop3actief = 1;
    }
  } else {
    knop3pressed = 0;
  }

  if(knop2actief == 1 && ingerold != 1 ) {
    inrollen();
  }
  else if(knop3actief == 1 && uitgerold != 1) {
    uitrollen();
  }
  if(loopcounter % 10 == 1) { //Every 1s
    sendCommand("baseRemand", basisRemand);
    sendCommand("inofuitrollen", inofuitrollen);
    berekenAfstand();
    if(afstand < 0) {
      afstand = 0;
    }
    
    module.setDisplayToDecNumber(gemRemand,0,false);
    
    if(autonoom == 0) {
      sensormeten = analogRead(sensor);
      Remand = sensormeten/5;
      i++;
      tijdRemand += Remand;
        if(i == 40) {
          gemRemand = (tijdRemand / 40);
          tijdRemand = 0;
          i = 0;
          sendCommand("remand", gemRemand);
        }
          // Als de gemiddelde Remand hoog ligt, wordt er uitgerold.
        if(gemRemand > basisRemand && uitgerold == 0 && gemRemand != 0) {
        uitrollen();
      }
      
      // Als de gemiddelde Remand laag ligt, wordt er ingerold.
      if(gemRemand <= basisRemand && ingerold == 0 && gemRemand != 0) {
        inrollen();
      }    
    }
    
  }

  
  if(ingerold == 1) {
    digitalWrite(groeneLed, HIGH);
    digitalWrite(geleLed, LOW);
  }
  else if(uitgerold == 1) {
    digitalWrite(rodeLed, HIGH);
    digitalWrite(geleLed, LOW);
  }
  
  if(inofuitrollen == 1) {
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
}


void inrollen() {
  uitgerold = 0;
  inofuitrollen = 1;
  digitalWrite(rodeLed, LOW);
  digitalWrite(groeneLed, HIGH);
  digitalWrite(geleLed, HIGH);
  delay(50);
  digitalWrite(geleLed, LOW);
  if (afstand > 50 && afstand != 0) {
    ingerold = 1;
    inofuitrollen = 0;  
    sendCommand("ingerold", ingerold);
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
  if(afstand < 5 && afstand != 0) {
    uitgerold = 1;
    inofuitrollen = 0;
    sendCommand("uitgerold", uitgerold);
  }
}

void sendCommand(String command, int data) {
  String commandString = command + " " + data;
  
  Serial.write(commandString.length());
  Serial.print(commandString);
}

