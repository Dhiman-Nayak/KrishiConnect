#include "DHT.h"

#define DHTPIN 2      // Use the pin number you've connected to the Data pin of DHT22
#define DHTTYPE DHT22 // DHT 22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

int light;
String hello;
float temperature, humidity;
// int led = 4;
int thresold = 170; // for ldr
int sensor_pin_fc28 = 2; 
int sensor_pin_fc37 = 1; 
int fc_28 ;
const int sensorMin = 0;     // sensor minimum for fc37
const int sensorMax = 1024;  // sensor maximum for fc37

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // pinMode(led, OUTPUT);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  light = analogRead(A0);
  
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  // Check if any reads failed and exit early (to try again).
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  fc_28= analogRead(sensor_pin_fc28);
  fc_28 = map(fc_28,550,0,0,100);
  int rain = analogRead(sensor_pin_fc37);

  hello = String(light) + "," + String(temperature) + "," + String(humidity) + "," + String(fc_28) + "," + String(rain);
  char helloCharArray[hello.length() + 1]; // +1 for null terminator
  hello.toCharArray(helloCharArray, hello.length() + 1);

  for (int i = 0; i < hello.length(); i++) {
    Serial.write(helloCharArray[i]);
  }
  Serial.write("\n"); 

  // if (light < thresold){
  //   digitalWrite(led, HIGH);
  // }
  // else{
  //   digitalWrite(led, LOW);
  // }
  delay(2000);
}
