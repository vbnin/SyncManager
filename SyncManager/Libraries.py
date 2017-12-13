#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Developeur : VBNIN - IPEchanges.
Ce fichier est une librairie requise par le script core.py
"""

import time
import os
import logging
from logging.handlers import RotatingFileHandler

# Activation du logger
handler = RotatingFileHandler('SyncManager.log', maxBytes=10000000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s : %(message)s'))
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(handler)

def Loop(Data):
    logger.info("Scan des dossiers...")
    List = [f for f in os.listdir(Data['WatchFld2'])]
    for f in os.listdir(Data['WatchFld1']):
        if f not in List:
            f = os.path.join(Data['WatchFld1'], f)
            os.remove(f)
            logger.info("Fichier supprimé : %s" % f)
        else:
            pass
    time.sleep(Data['LoopTime'])
