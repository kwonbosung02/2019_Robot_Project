void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}
 char get = ' ';
void loop() {
   
    
    get = Serial.read();      
    
    if(get == '3' || get == '4' || get == '5'){
      digitalWrite(13,HIGH);
      
      Serial.println(get);
    
    }
    else if(get == '0' || get == '1' || get == '2'){
      digitalWrite(13,LOW);
    }


 
}
