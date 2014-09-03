import re
import logging

from PyQt4.QtSql import *
from qgis.core import QgsRectangle
from qgis.core import QgsFeatureRequest

from vector_provider import VectorProvider


class ShapefileProvider(VectorProvider):

    def __init__(self, vector):
        VectorProvider.__init__(self, vector)
        self.logger = logging.getLogger('Vizitown')