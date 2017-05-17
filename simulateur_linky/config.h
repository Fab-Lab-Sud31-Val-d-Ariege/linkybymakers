/* 
 * Configuration globale du compteur.
 */

// Mode de fonctionnement du compteur. Au choix :
//  - 0 : historique, comme les compteurs pré-Linky
//  - 1 : standard, spécifique au compteur Linky
#define MODE_COMPTEUR 0

// Port série de sortie à utiliser. Au choix :
//  - Serial1 : sortie série sur broches 0 (Rx) et 1 (Tx)
//  - Serial  : sortie série USB, sur port "Programming Port)
#define SORTIE_SERIE Serial

#if MODE_COMPTEUR == 0
  // Inclusion des données de test du mode historique
  #include "historique_hc.h"
  #include "historique_hp.h"
  #include "historique_trame_tic.h"
#endif

#if MODE_COMPTEUR == 1
  // Inclusion des données de test du mode standard
#endif

// Macro de calcul du nombre d'éléments d'un tableau
#define TAILLE_TABLEAU(x)  (sizeof(x) / sizeof((x)[0]))
