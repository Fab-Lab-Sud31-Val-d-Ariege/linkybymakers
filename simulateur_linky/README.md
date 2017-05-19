Simulateur compteur Linky
==

Pré-requis
--

* Un Arduino / Genuino Zero

Fonctionnement général
--

Le simulateur Linky émet des trames TIC (Télé Information Consommateur) au
format historique ou au format standard en fonction de sa configuration. Les
trames sont émises sur la broche TX (1) de l'Arduino / Genuino Zero.


Organisation du code
--

* Fichier « simulateur_linky.ino » : code principal du simulateur.

* Fichier « config.h » : configuration du simulateur. Voir plus bas.

* Mode historique :
  * Fichier « historique_hc.h » contient une série d'index correspondant aux
    heures creuses.
  * Fichier « historique_hp.h » contient une série d'index correspondant aux
    heures pleines.
  * Fichier « historique_trame_tic.h » contient les différentes section de la
    trame TIC.
  * Notes :
    * Le nombre d'index HC et HP doit être identique.
    * La taille cumulée des fichiers « historique_hc.h » et « historique_hp.h »
      ne doit pas dépasser 200 ko.


* Mode standard :
  *  À définir


Configuration
--

Fichier « config.h » :
* « MODE_COMPTEUR » :
  * « 0 » pour simuleur un compteur électronique pré-Linky ou un compteur Linky en
    mode historique. La vitesse de la sortie série est dans ce cas de 1200 bps.
  * « 1 » pour un simulateur de compteur Linky en mode standard. La vitesse de
    sortie série est dans ce cas de 9600 bps.
* « SORTIE_SERIE » :
  * « Serial1 ». Les trames séries sont émises sur la broche 1 de l'Arduino /
    Genuino Zero.
  * « Serial ». Les trames séries sont émises sur la sortie USB « Programming
    Port » (marquée « DEBUG » sur la carte) de l'Arduino / Genuino Zero.


Licence
--

Ce code est distribué sous les termes de la licence GPL v3 (voir le fichier
LICENSE).
