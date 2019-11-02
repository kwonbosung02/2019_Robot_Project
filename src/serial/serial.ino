void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
}
char get = 0;

boolean check = false;
void loop() {
  
    digitalWrite(8,LOW);
    get = Serial.read();
    
    check_0(get);
    check_1000(get);
    check_2000(get);
    
 

    
    get = ' ';
    check = false;
    delay(50);
    delay(50);
}
