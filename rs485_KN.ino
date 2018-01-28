int number;
int val;
void setup() {
    Serial.begin(9600);
    pinMode(8, INPUT); //8 пин - в режиме входа. Кнопка корот на минус.
    digitalWrite(8, HIGH); //подключаем подтягивающий резистор 
    }
void loop() {
    if (Serial.available() > 0) {
    val = Serial.read();
    if(digitalRead(8)==HIGH)//если кнопка отключена и подается подтягивающее +5V ...
    {number = 1;Serial.write('1');} 
    if(digitalRead(8)==LOW) 
    {number = 0; Serial.write('0');} //если кнопка нажата и коротит на GND  ...
    }  
  }
