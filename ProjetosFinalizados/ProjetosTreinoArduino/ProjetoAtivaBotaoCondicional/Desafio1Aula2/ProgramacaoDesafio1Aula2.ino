
bool val1 = false;
bool val2 = false;

void setup(){

 pinMode(8, INPUT);
 pinMode(9, INPUT);
 pinMode(12, OUTPUT);
 pinMode(13, OUTPUT);

}

void loop() {


 val1 = digitalRead(8);
 val2 = digitalRead(9);

if(val1) digitalWrite(12,HIGH);
else if(val1 == false) digitalWrite(12,LOW);
if(val2) digitalWrite(13,HIGH);
else if(val2 == false) digitalWrite(13,LOW);



}
