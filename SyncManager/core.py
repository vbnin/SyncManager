#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Developeur : VBNIN - IPEchanges.
Script de synchronisation spécifique entre deux PC
"""

import os
import logging
from logging.handlers import RotatingFileHandler
import configparser
from argparse import ArgumentParser
from Libraries import Loop

# Activation du logger principal
try:
    handler = RotatingFileHandler('SyncManager.log', maxBytes=10000000, backupCount=5)
    handler.setFormatter(logging.Formatter('%(asctime)s : %(message)s'))
    logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
except:
    print("*"*10 + "Impossible d'initialiser le fichier de logs." + "*"*10)
    exit()

# Récupération des variables de démarrage
parser = ArgumentParser()
parser.add_argument("-c", "--config", dest="config", help="Fichier config.ini")
args = parser.parse_args()

# Lecture du fichier de Configuration et attribution des variables
try:
    config = configparser.ConfigParser()
    config.read(args.config)
    Data = {'WatchFld1':os.path.normpath(config.get('GENERAL', 'LocalWatchFolder')),
            'WatchFld2':os.path.normpath(config.get('GENERAL', 'RemoteWatchFolder')),
            'LoopTime':int(config.get('GENERAL', 'IntervalVerif')),
           }
except:
    logger.error("Fichier de configuration invalide ou introuvable. "
                   "Pour rappel : core.py -c config.ini")
    exit()

while True:
    Loop(Data)