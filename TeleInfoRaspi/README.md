# Mise en route de la lecture TéléInfo "Historique" sur Raspberry Pi 3


Dans le cadre du projet Linky by Makers nous commençons par récupérer des trames sur un compteur
électronique classique.

## Démodulateur
Basé sur un LTV-814 (0.22€ au lieu de 0.60€).
Pull-up de 10kΩ entre le 3.3V et l'optocoupleur.

Le LTV-814 a des temps de transition de 20µs au lieu de 4µs pour le SFH-620. À 1200 baud la durée d'un bit est de 833µs. À 9600 baud la durée d'un bit est de 104µs. Pas testé.


## Activation de l'UART sur les broches 8 at 10 du GPIO

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

#### En shell
A faire après chaque boot...

stty -F /dev/ttyAMA0 1200 cs7 evenp -cstopb -igncr -inlcr

Vérifier avec cat /dev/serial0 mais ne pas attendre de voir fidèlement tous les caractères des trames. Manque le mot d'état par exemple.

#### En python3
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


## Codes disponibles
Tous en python 3

* collectandstoreframes.py : écoute un compteur et stocke les octets reçus dans un fichier par jour.
* frames2csv.py : convertis un des fichiers précédents en ne coservant que les champs prcisés sur la lgne de commande.
* la-data.py : relis un fichier csv et trace les valeurs de colonnes dans un pdf.
