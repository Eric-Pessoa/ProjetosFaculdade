int buttonPinA = 2; // nomeia o pino2 do arduino como buttonPin2
int buttonPinB = 3; // nomeia o pino3 do arduino como buttonPin3
int potBaixo = A0;
int potCima = A1;

int buttonStatusA;  // Variavel de estado do buttonPin2
int buttonStatusB;  // Variavel de estado do buttonPin2

int ValPotCima;
int ValPotBaixo;

String c = "c";
String b = "b";



void setup() {
  pinMode(buttonPinA, INPUT_PULLUP);  //Pino2 como entrada com resistor de pullup interno
  pinMode(buttonPinB, INPUT_PULLUP);  //Pino3 como entrada com resistor de pullup interno
  Serial.begin(9600);				   //Inicialica a comunicação serial
}

void loop() {
  buttonStatusA = digitalRead(buttonPinA);
  buttonStatusB = digitalRead(buttonPinB);

  ValPotCima = analogRead(potCima);
  ValPotBaixo = analogRead(potBaixo);



  if ((buttonStatusA == LOW)){ 
    Serial.print(c +ValPotCima);
    delay(1000);                                            
  }

  if ((buttonStatusB == LOW)){
    Serial.print(b + ValPotBaixo);
    delay(1000);                                            

}

}