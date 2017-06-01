/* 
 * Configuration globale du configurateur BlueSmirf.
 */

// Broche TX utilisée pour communiquer avec le module BlueSmirf.
#define BT_SOFT_TX_PIN 2

// Broche RX utilisée pour communiquer avec le module BlueSmirf.
#define BT_SOFT_RX_PIN 3

// Broche TX utilisée pour communiquer avec le compteur Linky (non utilisée).
#define LK_SOFT_TX_PIN 8

// Broche RX utilisée pour communiquer avec le compteur Linky.
#define LK_SOFT_RX_PIN 9

// Vitesse de communication avec le module BlueSmirf.
# define BT_BAUD_RATE 9600

// Vitesse de communication avec le compteur.
//   1200 pour le mode historique
//   9600 pour le mode standard
# define LK_BAUD_RATE 1200

// Taille du buffer de lecture des données du compteur (en octets)
# define LK_BUFFER_SIZE 300
