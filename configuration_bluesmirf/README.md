Retransmetteur Linky vers Bluetooth
==

Pré-requis
--

* Un Arduino Mini Pro (modèle testé : ATmega168; 3,3V; 8 MHz)
* Un module Sparkfun BlueSmirf (modèle testé : Gold)
* Un compteur EDF ou le simulateur Linky

Les branchements sont les suivants :
* Arduino VCC -> BlueSmirf VCC
* Arduino GND -> BlueSmirf GND
* Arduino D2 -> BlueSmirf RX-I
* Arduino D3 -> BlueSmirf TX-I
* Arduino D9 -> Sortie TIC du compteur EDF / Simulateur D1


Fonctionnement général
--

Le retransmetteur Linky vers Bluetooth va avoir le fonctionnement suivant :
* Remplissage d'un buffer (300 octets par défaut) avec les données venant du compteur EDF ou du simulateur Linky
* Transmission du buffer en Bluetooth via l'émetteur BlueSmirf
* Mise en veille de 8 secondes


Organisation du code
--

* Fichier « retransmetteur_linky_bt.ino » : code principal du retransmetteur.

* Fichier « config.h » : configuration du retransmetteur. Voir plus bas.

Configuration
--

Fichier « config.h » :
* « SOFT_TX_PIN » : broche TX utilisée pour communiquer avec le module BlueSmirf.
* « SOFT_RX_PIN » : broche RX utilisée pour communiquer avec le module BlueSmirf.
* « INITIAL_BAUD_RATE » : vitesse de communication a utiliser avec le module BlueSmirf avant configuration.
  À adapter au fur et à mesure des configurations effectuées.
* « BAUD_RATE » : vitesse de communication avec le module BlueSmirf.
* « BT_NOM » : nom du module BlueSmirf.
* « BT_PIN » : code pin d'appairage du module BlueSmirf, 20 caractères max.


Licence
--

Ce code est distribué sous les termes de la licence GPL v3 (voir le fichier
LICENSE).
