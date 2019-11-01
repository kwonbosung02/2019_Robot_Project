void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
 int get = 0;
void loop() {
   
    
    get = Serial.read();
    check_0(get);



 
}
