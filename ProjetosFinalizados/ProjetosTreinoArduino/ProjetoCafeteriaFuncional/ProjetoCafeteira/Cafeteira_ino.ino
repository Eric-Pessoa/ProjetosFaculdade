#include <Ultrasonic.h>

int servoCompartimento = 9;
int servoTamanho = 10;
bool desligar;

HC_SR04 sensor1(2,3);
HC_SR04 sensor2(4,5);

int tamanho;
int compartimento;

int contador = 0;


void setup() {



 Serial.begin(9600);
 pinMode(servoCompartimento, OUTPUT);
 pinMode(servoTamanho, OUTPUT);
 pinMode(13, INPUT);




}

void loop() {

 desligar = digitalRead(13); 

 if(contador == 0) {
    //posição inicial do compartimento fechada
    	servoPos(9,0);
    //posição inicial do fazedor de café igual a 90
	servoPos(10, 90);
	delay(4000);
	contador += 1;
	Serial.print("Ligando...");
	
 } else if(desligar == false)  {
	servoPos(9,0);
     servoPos(10,90);
    } else {
    
    
    servoPos(9,0);
    servoPos(10,90);
	compartimento = sensor2.distance();
	tamanho = sensor1.distance();

	 if(compartimento <= 20) {
	  
	  servoPos(9,90);
	
	} else if (compartimento > 20) {
	
	  servoPos(9,0);
	
	}
	
	 if(tamanho >= 30) {
	  servoPos(10,0);
	  
	
	
	} else if ( tamanho < 30) {
	  
	  servoPos(10,180);
	
	}
	

   }

}







void servoPos(int servo, int dist){

	int micropulso = map(dist, 0, 180, 1000, 2000);
	digitalWrite(servo,HIGH);
	delayMicroseconds(micropulso);
	digitalWrite(servo,LOW);
	delay(1000);

}