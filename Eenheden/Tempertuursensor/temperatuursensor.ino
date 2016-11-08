// Initialiseer de poorten
const int groeneLed = 2;
const int geleLed = 3;
const int rodeLed = 4;
const int sensor = A0;
const int triggerPort = 8;
const int echoPort = 7;

// Defineer vriabelen
const float basisTemperatuur = 15.0;
int ingerold = 0;
int uitgerold = 0;
int afstand = 30;
int i = 0;
int tijdTemperatuur = 0;
int gemTemperatuur = 0;
int inofuitrollen = 0;
int metingen = 0;
// Start initialisatie loop
void setup() {
Serial.begin(9600);

for(int pinNumber = 2; pinNumber < 5; pinNumber++) {
  pinMode(pinNumber, OUTPUT);
  digitalWrite(pinNumber, LOW);
}
pinMode( triggerPort, OUTPUT );
pinMode( echoPort, INPUT );
}

void loop() {
  berekenAfstand();
  if(afstand < 0) {
    afstand = 0;
  }
  Serial.print("De afstand is: ");
  Serial.print(afstand);
  Serial.println(" cm.");


  int sensorWaarde = analogRead(sensor);
  float voltage = (sensorWaarde/1024.0) * 5;
  float temperatuur = ((voltage * 1000) - 500) / 10;
  i++;
    tijdTemperatuur += temperatuur;
  if(i == 40) {
    gemTemperatuur = (tijdTemperatuur / 40);
    tijdTemperatuur = 0;
    Serial.print("Gemiddelde temperatuur: ");
    Serial.println(gemTemperatuur);
    i = 0;
  }

  // Als de gemiddelde temperatuur hoog ligt, wordt er uitgerold.
  if(gemTemperatuur > basisTemperatuur && uitgerold == 0 && gemTemperatuur != 0) {
    uitrollen();
  }
  // Als de gemiddelde temperatuur laag ligt, wordt er ingerold.
  if(gemTemperatuur <= basisTemperatuur && ingerold == 0 && gemTemperatuur != 0) {
    inrollen();
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
    delay (500);
  }
  else {
    delay(1000);
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
    delay(500);
    digitalWrite(geleLed, LOW);
    if (afstand > 50 && afstand != 0) {
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
    delay(500);
    digitalWrite(geleLed, LOW);
    if(afstand < 5 && afstand != 0) {
    uitgerold = 1;
    inofuitrollen = 0;
  }
}


