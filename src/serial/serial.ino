void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
}
int get = 0;
boolean check = false;
void loop() {
    digitalWrite(8,LOW);
    get = Serial.parseInt();
    check_0(get);
    check_1000(get);
    check_2000(get);
    
 

    check = false;
    
}
