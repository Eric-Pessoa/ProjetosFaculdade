#include <Adafruit_SSD1306.h>
#define OLED_Address 0x3c
Adafruit_SSD1306 oled(128, 64);



int x=0, lastx=0, lasty=60, mais = 2, menos = 3, enter = 4, bomba = 9, 
aquecedor = 10, som = 11, led = 13, minDisplay = 0, segDisplay = 0, minDisplayLast = 0,
TermistorPin = A0, tempSetada, Vo;

float R1 = 10000, logR2, R2, T, Tc, Tf, temp, templast, timerlast,
c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;


unsigned long minuto=0, tempoEnter=0, setTempo = 0;

bool setTemp = true, setTimer = false;

void setup(){	
	Serial.begin(9600);
	oled.begin(SSD1306_SWITCHCAPVCC, OLED_Address);
 	oled.clearDisplay();
  	oled.setTextSize(1);
  	oled.setTextColor(WHITE);

	pinMode(mais, INPUT_PULLUP);
	pinMode(menos, INPUT_PULLUP);
	pinMode(enter, INPUT_PULLUP);
	pinMode(bomba, OUTPUT);
	pinMode(aquecedor, OUTPUT);
	pinMode(som, OUTPUT);
	pinMode(led, OUTPUT);
	pinMode(9, OUTPUT);
	pinMode(13, OUTPUT);
	Serial.begin(9600);
}


void loop(){

	temp = readTemp(TermistorPin);
	oledDisplay(temp, minuto, tempoEnter, minDisplay, tempSetada);
	
	if(digitalRead(mais) == LOW && setTemp == true){
		 tempSetada = tempSetada + 5;
	}
	
	if(digitalRead(menos) == LOW && setTemp == true){
		tempSetada = tempSetada- 5;
	}

	if(digitalRead(mais) == LOW && setTimer == true){
		minuto = minuto + 60000;
		minDisplay = minDisplay + 1;

	if (minDisplay > 59){
		minDisplay = 0;
		}
	}

	if(digitalRead(menos) == LOW && minuto > 0 && setTimer == true){
		minuto = minuto - 60000;
		minDisplay = minDisplay - 1;

	if (minDisplay < 0){
		minDisplay = 59;
		}
	}
	
	if(temp>0 && digitalRead(enter) == LOW && minuto >= 60000 && setTimer == true){
		digitalWrite(bomba, HIGH);
		digitalWrite(aquecedor, HIGH);
	}
	
	if (temp>=tempSetada){
		digitalWrite(aquecedor, LOW);
	}
	
	else if(temp<tempSetada && digitalRead(enter) == LOW && minuto >= 60000){
		digitalWrite(bomba, HIGH);
		digitalWrite(aquecedor, HIGH);
		tempoEnter = millis();
	}
	
	else if(digitalRead(bomba)== HIGH && digitalRead(aquecedor) == LOW && temp<tempSetada && setTimer == true){
		digitalWrite(aquecedor, HIGH);
	}
	
	
	if(digitalRead(enter) == LOW && setTemp == true){
		setTemp = !setTemp;
		setTimer = !setTimer;
		}		
	
	if(millis() - tempoEnter >= minuto && minuto >= 60000){
		digitalWrite(aquecedor, LOW);
		digitalWrite(bomba, LOW);

	if(digitalRead(led) == LOW && digitalRead(som) == LOW){
		digitalWrite(led, HIGH);
		digitalWrite(som, HIGH);
		tone(som, 600, 1000);
		}
		
	else{
		digitalWrite(led, LOW);
		digitalWrite(som, LOW);
		}
	}

	
	Serial.print("Tempo atual: ");Serial.print((millis()-tempoEnter)/1000);Serial.println(" s");
	Serial.print("Tempo setado: ");Serial.print(minuto/1000/3600);Serial.print(":");Serial.println(minDisplay);
	printTemp(temp);
	Serial.print("T atual: ");printTemp(temp);Serial.println(" C");
	Serial.print("T setada: ");Serial.print(tempSetada);Serial.println(" C");
	Serial.print("Status bomba: ");Serial.println(digitalRead(bomba));
	Serial.print("Status aquecedor: ");Serial.println(digitalRead(aquecedor));
	Serial.print("Botao enter Temperatura: ");Serial.println(setTemp);
	Serial.print("Botao enter Tempo: ");Serial.println(setTimer);
	delay(1000);
	}

float readTemp(int ThermistorPin){	
	Vo = analogRead(ThermistorPin);
	R2 = R1 * (1023.0/(float)Vo - 1.0);
	logR2 = log(R2);
	T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
	Tc = T - 273.15;
	return Tc;
}

void printTemp(float Tc){
	Serial.print("Temperatura: ");
	Serial.print(Tc);
	Serial.println(" C");
}

void oledDisplay(float temp, unsigned long minuto, unsigned long tempoEnter, int minDisplay, int tempSetado){
	oled.clearDisplay();
	oled.setCursor(0,0);
	oled.setTextColor(WHITE);
	oled.print("Temp setada: ");
	oled.print(tempSetado);
	oled.print("C: ");
	oled.println("");
	oled.print("Timer:  ");
	oled.print(minuto/1000/3600);oled.print(":");oled.print(minDisplay);
	
	unsigned long seg, min, hor, reg;
	reg = minuto/1000-(millis()-tempoEnter)/1000;
	seg = reg - int(reg/60)*60;
	min = int((reg)/60);
	hor = minuto/3600000-(millis()-tempoEnter)/3600000;
	oled.println("");

	
	if(digitalRead(bomba) == HIGH){
		oled.println("");
		oled.print("Tempo restante: ");
		oled.println("");
		oled.print(hor);oled.print(":");oled.print(min);oled.print(":");oled.print(seg);
		}	
		oled.display();
}


