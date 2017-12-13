#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Developeur : VBNIN - IPEchanges.
Script de synchronisation spécifique entre deux PC
"""

import logging
from logging.handlers import RotatingFileHandler
from Libraries import PrintException

# Activation du logger principal
try:
    handler = RotatingFileHandler('SyncManager.log', maxBytes=10000000, backupCount=5)
    handler.setFormatter(logging.Formatter('%(asctime)s : %(message)s'))
    logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(message)s')
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
except:
    PrintException("Impossible d'initialiser le fichier de logs.")
    exit()

