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

Afin de faciliter la détection des débuts et fin de buffer de retransmission, ce dernier est retransmis de la manière suivante :

    <saut de ligne>
    $ START $
    <saut de ligne>
    [la trame retransmise]
    <saut de ligne>
    $ END $
    <saut de ligne>


Organisation du code
--

* Fichier « retransmetteur_linky_bt.ino » : code principal du retransmetteur.

* Fichier « config.h » : configuration du retransmetteur. Voir plus bas.

Configuration
--

Fichier « config.h » :
* « BT_SOFT_TX_PIN » : broche TX utilisée pour communiquer avec le module BlueSmirf.
* « BT_SOFT_RX_PIN » : broche RX utilisée pour communiquer avec le module BlueSmirf.
* « LK_SOFT_TX_PIN » : broche TX utilisée pour communiquer avec le compteur Linky (non utilisée).
* « LK_SOFT_RX_PIN » : broche RX utilisée pour communiquer avec le compteur Linky.
* « BT_BAUD_RATE » : Vitesse de communication avec le module BlueSmirf.
* « LK_BAUD_RATE » : Vitesse de communication avec le compteur / simulateur
* « LK_BUFFER_SIZE » : Taille du buffer de lecture des données du compteur (en octets)


Licence
--

Ce code est distribué sous les termes de la licence GPL v3 (voir le fichier
LICENSE).
