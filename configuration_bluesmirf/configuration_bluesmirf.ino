#include "config.h"
#include <SoftwareSerial.h>

SoftwareSerial blueSmirf(SOFT_RX_PIN, SOFT_TX_PIN);

void setup() {
  Serial.begin(9600);

  Serial.println("*** Prêt");

  blueSmirf.begin(INITIAL_BAUD_RATE);

  Serial.println("*** Passage en mode commande");
  // Passage en mode commande
  blueSmirf.print("$$$");

  delay(1000);

  while(blueSmirf.available())
  {
    Serial.print((char)blueSmirf.read());
  }


  Serial.println("*** Changement du nom");
  // Changement du nom
  blueSmirf.print("SN,");
  blueSmirf.print(BT_NOM);
  blueSmirf.print("\n");
  delay(1000);

  while(blueSmirf.available())
  {
    Serial.print((char)blueSmirf.read());
  }


  Serial.println("*** Changement du code pin");
  // Changement du code pin
  blueSmirf.print("SP,");
  blueSmirf.print(BT_PIN);
  blueSmirf.print("\n");
  delay(1000);

  while(blueSmirf.available())
  {
    Serial.print((char)blueSmirf.read());
  }


  Serial.println("*** Changement de la vitesse");
  // Changement de la vitesse du port
  blueSmirf.print("SU,");
  blueSmirf.print(BAUD_RATE);
  blueSmirf.print("\n");
  delay(1000);

  while(blueSmirf.available())
  {
    Serial.print((char)blueSmirf.read());
  }


  Serial.println("*** Redémarrage");
  blueSmirf.print("R,1");
  delay(1000);

}

void loop() {
  // On ne fait rien.
  delay(1000);
}
