import json
import logging

from converter import Converter

from qgis.core import QgsRectangle
from qgis.core import QgsFeatureRequest


class VectorProvider:

    NO_HEIGHT = "0"
    HEIGHT = "height"
    DATA = "data"
    TYPE_JSON = "type"
    COORDINATES_JSON = "coordinates"
    MULTI = "Multi"

    # POINT
    POINT_1 = "Point"
    POINT_2 = "MultiPoint"
    POINT_JS = "point"

    # LINE
    LINE_1 = "MultiLineString"
    LINE_2 = "LineString"
    LINE_JS = "line"

    # POLYGON
    POLYGON_1 = "Polygon"
    POLYGON_2 = "MultiPolygon"
    POLYGONE_JS = "polygon"

    def __init__(self, vector):
        self._vector = vector
        self._converter = Converter()
        self.logger = logging.getLogger('Vizitown')

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

            if self._vector.has_column_color():
                d[self.DATA] = feature.attribute(self.vector._get_column_color())

            geojson = json.loads(feature.geometry().exportToGeoJSON())
            geom_type = geojson[self.TYPE_JSON]
            coordinates = geojson[self.COORDINATES_JSON]
            if _is_multi(geom_type):
                # Multi part geom
                for
            else:
                # Simple part geom
            d[self.COORDINATES_JSON] = self._read_geojson()
            ret_tile.append(d)

        #self.logger.debug(ret_tile)
        return ret_tile

    def _read_coordinates(self, array):
        #self.logger.debug(geom)
        return None

    def _is_multi(self, geometry_type):
        return geometry_type.startswith(self.MULTI)

    def _is_point(self, gtype):
        return gtype == self.POINT_1 || gtype == self.POINT_2

    def _is_line(self, gtype):
        return gtype == self.LINE_1 || gtype == self.LINE_2

    def _is_polygon(self, gtype):
        return gtype == self.POLYGON_1 || gtype == self.POLYGON_2

    def _can_convert(self):
        return True
