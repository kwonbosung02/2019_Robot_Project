void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
 int get = 0;
void loop() {
   
    get = Serial.parseInt();
    check_0(get);
    check_1000(get);
    check_2000(get);
    delay(300);
}
