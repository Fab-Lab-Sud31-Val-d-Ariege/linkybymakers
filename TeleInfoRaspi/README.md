# Lecture TéléInfo "Historique" sur Raspberry Pi 3

Dans le cadre du projet Linky by Makers nous commençons par récupérer des trames sur un compteur électronique classique.

## Lecture filaire

### Démodulateur
Basé sur un LTV-814 (0.22€ au lieu de 0.60€).
Pull-up de 10kΩ entre le 3.3V et l'optocoupleur.

Le LTV-814 a des temps de transition de 20µs au lieu de 4µs pour le SFH-620. À 1200 baud la durée d'un bit est de 833µs. À 9600 baud la durée d'un bit est de 104µs. Pas testé.


### Activation de l'UART sur les broches 8 at 10 du GPIO

Sources :
- http://www.framboise314.fr/le-port-serie-du-raspberry-pi-3-pas-simple/
- http://www.journaldulapin.com/2016/02/25/raspberry-pi-teleinfo/
- http://www.magdiblog.fr/gpio/teleinfo-edf-suivi-conso-de-votre-compteur-electrique/
- http://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/
- Et moi même...



### Modification du fichier /boot/config.txt
La fin du fichier se présente ainsi :

    # Serial GPIO is needed
    enable_uart=1
    # disable bluetooth and reuse the real UART
    dtoverlay=pi3-disable-bt
    #dtoverlay=pi3-miniuart-bt

### Modification du fichier /boot/cmdline.txt
Supprimer `console=serial0,115200`

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait

### Paramétrage du port série pour récupérer les trames
Mode 1200 7E1

### En shell
A faire après chaque boot...

    stty -F /dev/ttyAMA0 1200 cs7 evenp -cstopb -igncr -inlcr

Vérifier avec cat /dev/serial0 mais ne pas attendre de voir fidèlement tous les caractères des trames. Manque le mot d'état par exemple.

### En python3
Les `<cr>` `<lf>` `<stx>` `<etx>` sont passés tels quels. Le code suivant a bien fonctionné (trouvé sur internet et adapté à Python3).


    import sys
    import serial

    instream = serial.Serial(port="/dev/ttyAMA0", baudrate=1200, \
    bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, \
    stopbits=serial.STOPBITS_ONE)

    while True :
        cc = instream.read(1)
        #print("> {0} <".format(cc))
        if cc == b'\x02' :
            sys.stdout.write("\n====== STX")
        elif cc == b'\x03' :
            sys.stdout.write("\n====== ETX")
        else :
            sys.stdout.write(cc.decode("ascii"))


Résultat dans la console :

    ====== STX
    ADCO 030422000048 .
    OPTARIF HC.. <
    ISOUSC 30 9
    HCHC 036433204 _
    HCHP 039695921 ?
    PTEC HP..
    IINST 002 Y
    IMAX 031 C
    TENSION 245 ;
    PAPP 00410 &
    HHPHC A ,
    MOTDETAT 000000 B
    ====== ETX


## Lecture Bluetooth

La lecture Bluetooth permet de récupérer les trames venant de retransmetteur Linky vers Bluetooth

### Pré-requis

* Un Raspberry Pi 3 avec Raspbian installé et à jour.
* Un retransmetteur Linky vers Bluetooth, qu'il soit branché à un compteur ou un simulateur.

La suite des commandes sera effectuée en ligne de commande depuis le Raspberry Pi.

### Lancement la console Bluetooth

    sudo bluetoothctl

### Activation de l'agent

    agent on
    default-agent

### Lancement du scan des périphériques à proximité

    scan on

Attendre que l'émetteur BT apparaisse, du type :

    [NEW] Device 00:06:66:82:7C:41 LinkyByMakersBT

Noter l'adresse du périphérique, dans ce cas "00:06:66:82:7C:41".

### Arrêt du scan

    scan off

### Appairage de l'émetteur Bluetooth

    pair [adresse_peripherique]

La réponse type attendue est de la forme :

    Attempting to pair with [adresse_peripherique]
    [CHG] Device [adresse_peripherique] Connected: yes
    Request confirmation
    [agent] Confirm passkey 516653 (yes/no): yes
    [CHG] Device [adresse_peripherique] UUIDs:
      00001101-0000-1000-8000-00805f9b34fb
    [CHG] Device [adresse_peripherique] Paired: yes
    Pairing successful
    [CHG] Device [adresse_peripherique] Connected: no

### Autoriser l'appairage automatique pour ce périphériques

    trust [adresse_peripherique]

La réponse type attendue est :

    [CHG] Device [adresse_peripherique] Trusted: yes
    Changing [adresse_peripherique] trust succeeded

### Quitter la console BT
    quit


### Création du périphérique série permettant de communiquer avec l'émetteur Bluetooth
    sudo modprobe rfcomm
    sudo rfcomm bind rfcomm0 [adresse_peripherique]

Ajouter ces lignes dans le fichier /etc/rc.local pour que la création du périphérique série se fasse à chaque reboot

    sudo nano /etc/rc.local

(à mettre avant la ligne exit 0)

Pour vérifier que ça fonctionne :

    cat /dev/rfcomm0

Des salves de données venant de l'émetteur BT doivent apparaitre toutes les 8 secondes



## Organisation du code

À utiliser avec Python 3.x

* collectandstoreframes.py : écoute un compteur et stocke les octets reçus dans un fichier par jour.
* frames2csv.py : convertis un des fichiers précédents en ne coservant que les champs prcisés sur la lgne de commande.
* la-data.py : relis un fichier csv et trace les valeurs de colonnes dans un pdf.
* collectandstorefrombt.py : relis un fichier (data/simulateur_raw.dat), test pour la capture des trames via Bluetooth.
