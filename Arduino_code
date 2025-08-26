 const int potPin=A1;
 const int lm35Pin=A0;
 const int ledPin=9;

void setup() {
  Serial.begin(9600);
pinMode(ledPin,OUTPUT);

}

void loop() {
int analogDeger=analogRead(lm35Pin);
  float voltaj=analogDeger*(5.0/1023);
  float sicaklik=voltaj*10.0;

int potDeger=analogRead(potPin);
  int parlaklik=map(potDeger,0,1023,0,255);
analogWrite(ledPin,parlaklik);

  Serial.print(sicaklik);
  Serial.print(",");
  Serial.println(potDeger);
  delay(500);



}
