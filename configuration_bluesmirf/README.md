Configurateur BlueSmirf
==

Pré-requis
--

* Un Arduino Mini Pro (modèle testé : ATmega168; 3,3V; 8 MHz)
* Un module Sparkfun BlueSmirf (modèle testé : Gold)

Les branchements sont les suivants :
* Arduino VCC -> BlueSmirf VCC
* Arduino GND -> BlueSmirf GND
* Arduino D2 -> BlueSmirf RX-I
* Arduino D3 -> BlueSmirf TX-I


Fonctionnement général
--

Le configurateur BlueSmirf va configurer un module éponyme avec les paramètres suivants :
* Vitesse : 9600 bps
* Nom : LinkyByMakersBT
* Clé appairage : 3113


Organisation du code
--

* Fichier « configuration_bluesmirf.ino » : code principal du simulateur.

* Fichier « config.h » : configuration du configurateur. Voir plus bas.

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
