#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Developeur : VBNIN - IPEchanges.
Ce fichier est une librairie requise par le script core.py
"""

import logging
from logging.handlers import RotatingFileHandler

# Activation du logger
handler = RotatingFileHandler('SyncManager.log', maxBytes=10000000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s : %(message)s'))
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(handler)

# Définition de la fonction PrintException
def PrintException(msg):
    print("*" * 40)
    print(msg)
    print("*" * 40)
