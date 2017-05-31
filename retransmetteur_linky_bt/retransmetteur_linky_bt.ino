#include "config.h"
#include <avr/power.h>
#include <avr/sleep.h>

#include <SoftwareSerial.h>
#include <Adafruit_SleepyDog.h>

SoftwareSerial blueSmirf(BT_SOFT_RX_PIN, BT_SOFT_TX_PIN);
SoftwareSerial linky(LK_SOFT_RX_PIN, LK_SOFT_TX_PIN);

void setup() {
  // Économies d'énergie, on désactive les périphériques inutiles (ADC, SPI, I2C)
  power_adc_disable();
  power_spi_disable();
  power_twi_disable();
}

void loop() {
  char buffer[LK_BUFFER_SIZE] = "";

  // On lit une série de donnée venant du compteur (buffer de LK_BUFFER_SIZE octets)
  linky.begin(LK_BAUD_RATE);
  delay(1000);

  int i=0;
  while (linky.available() && i < LK_BUFFER_SIZE - 1) {
    buffer[i] = linky.read();
    i++;
    delay(1);
  }
  // Caractère de fin de chaine
  buffer[LK_BUFFER_SIZE - 1] = 0;

  linky.end();

  // On transmet les données lue du compteur Linky via BT
  blueSmirf.begin(BT_BAUD_RATE);
  for (int i = 0 ; i <= LK_BUFFER_SIZE ; i++) {
    blueSmirf.write(buffer[i]);
  }
  blueSmirf.end();
  
  
  // Mise en sommeil pour 8 secondes (le max pour la plateforme cible).
  Watchdog.sleep(8000);
}
