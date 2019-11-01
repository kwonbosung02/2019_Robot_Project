void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
 char get = 0;
void loop() {
   
    
    get = Serial.parseInt();

    check_0((int)get);
    delay(300);


 
}
