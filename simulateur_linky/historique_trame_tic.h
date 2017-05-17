/* Exemple de trame en mode historique
 *  
 * Chaque ligne de trame commence par le caractères \n
 *   et se termine par le caractère \r.
 *   
 * Spécifications des trames en mode historique :
 *   http://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_02E.pdf
 *
 * ADCO 030422000048  .
 * OPTARIF HC.. <
 * ISOUSC 30 9
 * HCHC 036395657 2
 * HCHP 039661265 9
 * PTEC HC.. S
 * IINST 011 Y
 * IMAX 031 C
 * PAPP 02570 /
 * HHPHC A ,
 * MOTDETAT 000000 B
 */

const char adresseCompteur[]       = "\nADCO 030422000048 .\r"; // Adresse du compteur
const char optionTarif[]           = "\nOPTARIF HC.. <\r";      // Option tarifaire choisie
const char intensiteContrat[]      = "\nISOUSC 30 9\r";         // Intensité souscrite
const char indexHC[]               = "\nHCHC ";               // Index heures creuses
const char indexHP[]               = "\nHCHP ";               // Index heures pleines
const char periodeTarifEnCoursHC[] = "\nPTEC HC.. S\r";         // Période tarifaire en cours (cas heures creuses)
const char periodeTarifEnCoursHP[] = "\nPTEC HP.. S\r";         // Période tarifaire en cours (cas heures pleines)
const char intensiteInstantanee[]  = "\nIINST 011 Y\r";         // Intensité instantanée
const char intensiteMax[]          = "\nIMAX 031 C\r";          // Intensité maximale appelée
const char puissanceApparente[]    = "\nPAPP 02570 /\r";        // Puissance apparente
const char horairesHPHC[]          = "\nHHPHC A ,\r";           // Horaire heures pleines heures creuses
const char motEtat[]               = "\nMOTDETAT 000000 B\r";   // Mot d'état du compteur
