from qgis.core import QgsRectangle
from qgis.core import QgsFeatureRequest

from .. import core


class VectorProvider:

    NO_HEIGHT = "0"
    HEIGHT = "HEIGHT"
    COORDINATES = "coordinates"

    def __init__(self, vector):
        self._vector = vector
        self.logger = core.Logger.instance()

    ## get_column_info metho
    # Gives all data column name + data type
    # @return A dict such as {attribute name: attribute type}
    def get_columns_info(self):
        attributes = self._vector._qgisLayer.pendingFields().toList()
        result = {}
        for a in attributes:
            result[a.name()] = a.typeName()
        return result

    def add_column2(self, name, type):
        self._vector._column2_name = name
        self._vector._column2_type = type

    def request_tile(self, tile):
        self.logger.debug("Request Tile Vector Provider")
        self._vector.update_color()

        if self._vector._column2_is_geom:
            self.logger.warning("Geometry is 3D cannot handle in vector provider")
            return

        # QgsRectangle (double xmin=0, double ymin=0, double xmax=0, double ymax=0)
        rect = QgsRectangle(tile.xmin, tile.ymin, tile.xmax, tile.ymax)

        features = self._vector._qgisLayer.getFeatures(QgsFeatureRequest().setFilterRect(rect))

        ret_tile = []

        for feature in features:
            d = {}
            if self._vector._has_2_column:
                d[self.HEIGHT] = feature.attribute(self._vector._column2_name)
            else:
                d[self.HEIGHT] = self.NO_HEIGHT

            d[self.COORDINATES] = self._read_geo_json(feature.geometry().exportToGeoJSON())
            ret_tile.append(d)

        self.logger.debug(ret_tile)
        return ret_tile

    def _read_geo_json(self, geojson):
        return None