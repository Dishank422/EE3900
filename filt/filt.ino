#include<ArduinoJson.h>

StaticJsonDocument<72000> rec;

double x = 0;
double x_1 = 0;
double x_2 = 0;
double x_3 = 0;
double x_4 = 0;
double y = 0;
double y_1 = 0;
double y_2 = 0;
double y_3 = 0;
double y_4 = 0;

void setup() {
	Serial.begin(115200);
	delay(1000);
}

void loop() {
  while(!Serial) continue;
  String tmp2;
  String tmp;
  tmp = Serial.readStringUntil('\n');
  deserializeJson(rec, tmp);
  for(int i=0; i < 600; i++)
  {
    x = rec["d"][i];
    y = 0.00345416*x + 0.01381663*x_1 + 0.02072494*x_2 + 0.01381663*x_3 + 0.00345416*x_4 + 2.5194645*y_1 - 2.56083711*y_2 + 1.20623537*y_3 - 0.22012927*y_4;
    y_4 = y_3;
    y_3 = y_2;
    y_2 = y_1; 
    y_1 = y;
    x_4 = x_3;
    x_3 = x_2;    
    x_2 = x_1;
    x_1 = x;
    rec["d"][i] = x;
  }
	serializeJson(rec, tmp2);
  Serial.println(tmp2);  
  rec.clear();
}
