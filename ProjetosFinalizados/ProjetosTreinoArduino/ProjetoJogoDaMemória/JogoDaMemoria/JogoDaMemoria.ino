long Random;
int contador = 0;
int led1 = 7;
int led2 = 8; 
int led3 = 12;
int varNivel = 2;
String texto;
String sequenciaCerta;

void setup() {

  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);




}

void loop() {

  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(12, LOW);
	
	
  while(contador <= varNivel){
    Serial.println("Voce esta no nivel: ");
    Serial.println(varNivel);
    Random = random(3);
  	digitalWrite(7, LOW);
  	digitalWrite(8, LOW);
  	digitalWrite(12, LOW);
	
    switch(Random){
    case 0:
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
      delay(1000);
      contador += 1;
      sequenciaCerta = String(sequenciaCerta + "1");
      break;
    case 1:
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, LOW);
      delay(1000);
      contador += 1;
      sequenciaCerta = String(sequenciaCerta + "2");
      break;
    case 2:
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, HIGH);
      delay(1000);
      contador += 1;
      sequenciaCerta = String(sequenciaCerta + "3");
      break;
    }
}

  if(Serial.available() && (contador - 1) == varNivel) {
    texto = Serial.readString();
    if(texto.equals(sequenciaCerta)) {
	  Serial.println("Resposta certa! próximo nivel.");
      varNivel += 1;
	  contador = 0;
	  sequenciaCerta = "";
	  texto = "";
    }
    else if(!texto.equals(sequenciaCerta)) {
	  Serial.println("Errou a resposta. Volta do comeco.");
      varNivel = 2;
	  contador = 0;
	  sequenciaCerta = "";
	  texto = "";
      
    }
    
        
  }     
  
  }



