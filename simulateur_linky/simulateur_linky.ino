#include "config.h"

void setup() {
  if (MODE_COMPTEUR == 0) {
    // La sortie téléinfo du compteur Linky fonctionne à 1200 bauds en mode historique
    SORTIE_SERIE.begin(1200);
  } else if (MODE_COMPTEUR == 1) {
    // La sortie téléinfo du compteur Linky fonctionne à 9600 bauds en mode standard
    SORTIE_SERIE.begin(9600);
  }

  // Initialise le générateur pseudo-aléatoire
  randomSeed(analogRead(0));
}

void loop() {
  genereTrame();
}

#if MODE_COMPTEUR == 0
// Mode historique
void genereTrame() {
  // On boucle sur l'ensemble des index HP ou HC
  for (int indexNumber = 0 ; indexNumber < TAILLE_TABLEAU(hcIndexes) ; indexNumber++) {
    // Début de trame (caractère STX)
    SORTIE_SERIE.write(0x02);
    
    // Adresse du compteur
    SORTIE_SERIE.print(adresseCompteur);

    // Option tarifaire choisie
    SORTIE_SERIE.print(optionTarif);

    // Intensité souscrite
    SORTIE_SERIE.print(intensiteContrat);

    // Index heures creuses
    SORTIE_SERIE.print('\n');
    SORTIE_SERIE.print(indexHC);
    SORTIE_SERIE.print(hcIndexes[indexNumber]);
    SORTIE_SERIE.print(" ");
    char data[15] = "";
    strcat(data, indexHC);
    strcat(data, hcIndexes[indexNumber]);
    SORTIE_SERIE.write(checksumTic(data));
    SORTIE_SERIE.print('\r');

    // Index heures pleines
    SORTIE_SERIE.print('\n');
    SORTIE_SERIE.print(indexHP);
    SORTIE_SERIE.print(hpIndexes[indexNumber]);
    SORTIE_SERIE.print(" ");
    strcpy(data, "");
    strcat(data, indexHP);
    strcat(data, hpIndexes[indexNumber]);
    SORTIE_SERIE.write(checksumTic(data));
    SORTIE_SERIE.print('\r');

    // Période tarifaire en cours
    SORTIE_SERIE.print(periodeTarifEnCoursHC);

    // Intensité instantanée
    SORTIE_SERIE.print(intensiteInstantanee);

    // Intensité maximale appelée
    SORTIE_SERIE.print(intensiteMax);

    // Puissance apparente
    SORTIE_SERIE.print(puissanceApparente);

    // Horaire heures pleines heures creuses
    SORTIE_SERIE.print(horairesHPHC);

    // Mot d'état du compteur
    SORTIE_SERIE.print(motEtat);

    // Fin de trame
    SORTIE_SERIE.write(0x03);

    // Le delai entre chaque trame est compris entre 16 et 33 ms
    delay (random(16,33));
  }
}
#endif

#if MODE_COMPTEUR == 1
// Mode standard
void genereTrame() {
  SORTIE_SERIE.println("Non implémenté");

  delay (100);
}
#endif

// Calcul du checksum d'une trame TIC
byte checksumTic(char data[]) {
  int sum = 0;
  for (byte i = 0 ; i < strlen(data) ; i++) {
    sum += data[i];
  }
  sum = sum & byte(0x3F);
  sum += byte(0x20);

  return byte(sum);
}

