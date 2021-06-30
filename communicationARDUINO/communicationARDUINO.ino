#include<Servo.h>
Servo myservo;
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4); 

void setup() {
pinMode(4, INPUT_PULLUP);
pinMode(5, INPUT_PULLUP);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Welcome to the");
  lcd.setCursor(4,1);
  lcd.print("Parking!");  
myservo.attach(9);
}

void loop() {
if(digitalRead(4)==LOW)
  {
  lcd.init();  
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Parking Status :");
  lcd.setCursor(5,1);
  lcd.print("EMPTY");  
  myservo.write(0);   
  delay(5000);
  myservo.write(90);   
  delay(5000); 
  }
while(digitalRead(5)==LOW)
  {
  lcd.init();  
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Parking Status :");
  lcd.setCursor(6,1);
  lcd.print("FULL");
  
  }
  
  myservo.write(90);
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Welcome to the");
  lcd.setCursor(4,1);
  lcd.print("Parking!");  
}
