#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT);

long dadoCima;
long dadoBaixo;

void setup() {
  Serial.begin(9600);				   
  oled.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);
  oled.clearDisplay();
}


void loop() {
  
  if(Serial.available()) {

	
	if(Serial.read() == 'c'){
  		dadoCima = Serial.parseInt();
	}
	else {
	 	dadoBaixo = Serial.parseInt();
	}

  }
	
  Serial.println(String("Pot1: ") + dadoCima);
  Serial.println(String("Pot2: ") + dadoBaixo);


  oled.clearDisplay();
  oled.setTextSize(1);
  oled.setTextColor(SSD1306_WHITE);
  oled.setCursor(0, 0); 
  oled.print("Potenciometro 1: ");
  oled.println(dadoCima);
  oled.print("Potenciometro 2: ");
  oled.println(dadoBaixo);
  oled.display();

 

 


}
