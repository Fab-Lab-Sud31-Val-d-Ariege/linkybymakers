#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Test du port série
import serial
test_string = bytes("Je teste le port série 1 2 3 4 5", "UTF-8")
port_list = ["/dev/ttyAMA0", "/dev/ttyAMA0", "/dev/ttyS0", "/dev/ttyS0",]
for port in port_list:
    try:
        serialPort = serial.Serial(port, 9600, timeout = 2)
        print ("Port Série {0} ouvert pour le test :".format(port))
        bytes_sent = serialPort.write(test_string)
        print ("Envoyé {0} octets".format(bytes_sent))
        loopback = serialPort.read(bytes_sent)
        if loopback == test_string:
            print ("Reçu {0} octets identiques. Le port {1} fonctionne bien !".format(len(loopback), port))
        else:
            print ("Reçu des données incorrectes : {0} sur le port série {1} bouclé".format(loopback, port))
        serialPort.close()
    except IOError:
        print ("Erreur sur {0}".format(port))
