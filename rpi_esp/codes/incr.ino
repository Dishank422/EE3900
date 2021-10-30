int num = 0;

void setup() {
	Serial.begin(9600);
	delay(1000);
}

void loop() {
	if(Serial.available()){
		num = Serial.read();
		delay(20);
		Serial.println(num+1);  
	}
}
