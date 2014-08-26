import re

from PyQt4.QtSql import *
from qgis.core import QgsRectangle
from qgis.core import QgsFeatureRequest

from .. import core

from vector_provider import VectorProvider


class ShapefileProvider(VectorProvider):

    def __init__(self, vector):
        VectorProvider.__init__(self, vector)
        self.logger = core.Logger.instance()

    def request_tile(self, tile):
        self._vector.update_color()
        VectorProvider.request_tile(self, tile)