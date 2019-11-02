int check_0(int get){
  if(get > 0) check = true;
  if(get == 0) {Serial.println("NaN");
    noTone(9);
  }
  
  if(get == 1) {Serial.println("item = 1"); 
     tone(9,261); 
  }
  if(get == 2) {Serial.println("item = 2");
    tone(9,294);
  }
  if(get == 3) {Serial.println("item = 3");
    tone(9,330);
  }
  if(get == 4) {Serial.println("item = 4"); 
    tone(9,349);
  }
  if(get == 5) {Serial.println("item = 5");
    tone(9,440);
  }
  if(check == true){
    digitalWrite(8,HIGH);
  }
  
}
