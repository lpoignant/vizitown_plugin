# -*- coding: utf-8 -*-
"""
/***************************************************************************
VizitownDialog
                                A QGIS plugin
2D to 3D
                            -------------------
        begin                : 2014-01-09
        copyright            : (C) 2014 by Cubee(ESIPE)
        email                : vizitown@gmail.com
***************************************************************************/

/***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************/
"""

import logging
import sys
import os

from logging import handlers


## classFactory load Vizitown class from file Vizitown
def classFactory(iface):
    logger = logging.getLogger('Vizitown')
    logger.setLevel(logging.DEBUG)

    # Define file with entire path
    loggerPath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "vizitown.log")

    fh = logging.handlers.RotatingFileHandler(loggerPath, mode='a', maxBytes=5000000, backupCount=5)

    fh.setLevel(logging.DEBUG)

    format = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
    formatter = logging.Formatter(format)

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    sys.stderr = open(os.path.join(os.path.dirname(__file__), "log.err"), "w", 0)
    sys.stdout = open(os.path.join(os.path.dirname(__file__), "log.out"), "w", 0)

    from vizitown import Vizitown
    return Vizitown(iface)
