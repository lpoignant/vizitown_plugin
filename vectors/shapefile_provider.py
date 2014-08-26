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

        # QgsRectangle (double xmin=0, double ymin=0, double xmax=0, double ymax=0)
        rect = QgsRectangle(tile.xmin, tile.ymin, tile.xmax, tile.ymax)

        features = self._vector._qgisLayer.getFeatures(QgsFeatureRequest().setFilterRect(rect))

        for feature in features:
            self.logger.debug(feature.geometry().exportToGeoJSON())