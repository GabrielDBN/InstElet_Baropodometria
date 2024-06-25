void setup(void) {
  Serial.begin(115200);   
}

void loop(void) {
  float analogValue1 = analogRead(26); // sensor 6
  float force1 = analogValue1 * (20.0 / 1023.0);
  
  float analogValue2 = analogRead(35); // sensor 5
  float force2 = analogValue2 * (20.0 / 1023.0);
  
  float analogValue3 = analogRead(25); // sensor 4
  float force3 = analogValue3 * (20.0 / 1023.0);
  
  float analogValue4 = analogRead(32); // sensor 3
  float force4 = analogValue4 * (20.0 / 1023.0);
  
  float analogValue5 = analogRead(33); // sensor 2
  float force5 = analogValue5 * (20.0 / 1023.0);
  
  float analogValue6 = analogRead(27); // sensor 1
  float force6 = analogValue6 * (20.0 / 1023.0);

  // Enviar todos os valores de força na mesma linha separados por vírgulas
  Serial.print(force1);
  Serial.print(",");
  Serial.print(force2);
  Serial.print(",");
  Serial.print(force3);
  Serial.print(",");
  Serial.print(force4);
  Serial.print(",");
  Serial.print(force5);
  Serial.print(",");
  Serial.print(force6);
  Serial.println();

  delay(500);
}