
bool val1 = false;

void setup(){


 Serial.begin(9600);  // inicia a porta serial, configura a taxa de dados para 9600 bps​
 pinMode(9, INPUT);
 pinMode(13, OUTPUT);

}

void loop() {

 val1 = digitalRead(9);

if(val1) {digitalWrite(13,LOW); 
	Serial.println("Desligado");}
if(val1 == false) {digitalWrite(13,HIGH); 
	Serial.println("ligado");}




}