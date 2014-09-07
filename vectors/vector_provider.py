import json
import logging

from converter import Converter

from qgis.core import QgsRectangle
from qgis.core import QgsFeatureRequest


##  VectorProvider class
#   TODO
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

    ##  Constructor
    #   @param vector
    def __init__(self, vector):
        self._vector = vector
        self._converter = Converter()
        self.logger = logging.getLogger('Vizitown')

    ##  get_column_info metho
    #   Gives all data column name + data type
    #   @return A dict such as {attribute name: attribute type}
    def get_columns_info(self):
        attributes = self._vector._qgisLayer.pendingFields().toList()
        result = {}
        for a in attributes:
            result[a.name()] = a.typeName()
        return result

    ##  add_column2 method
    #   TODO
    #   @param name
    #   @param type
    def add_column2(self, name, type):
        self._vector._column2_name = name
        self._vector._column2_type = type

    ##  request_tile method
    #   TODO
    #   @param tile
    #   @return an array
    def request_tile(self, tile):
        self._vector.update_color()

        if self._vector._column2_is_geom:
            self.logger.warning("3D geometry cannot handle in vector provider")
            return

        self._vector.define_geometry()
        # QgsRectangle (double xmin=0, double ymin=0, double xmax=0, double ymax=0)
        rect = QgsRectangle(tile.xmin, tile.ymin, tile.xmax, tile.ymax)

        features = self._vector._qgisLayer.getFeatures(QgsFeatureRequest().setFilterRect(rect))
        result = self._read_features(features)

        if not self._can_convert():
            self.logger.error("Impossible to convert data from vector : " + self._vector._display_name)

        sort = self._vector._color.sort_result(result)

        geometry = self._vector._geometry
        dim = self._vector._dimension
        uuid = self._vector._uuid
        convert = self._converter.convert(sort, geometry, dim, uuid)

        # In future the message will probably send to browser from here

        return convert

    ##  _read_features method
    #   TODO
    #   @param features
    #   @return an array
    def _read_features(self, features):
        ret_tile = []

        for feature in features:
            d = {}
            if self._vector._has_2_column:
                d[self.HEIGHT] = feature.attribute(self._vector._column2_name)
            else:
                d[self.HEIGHT] = self.NO_HEIGHT

            if self._vector.has_column_color():
                d[self.DATA] = feature.attribute(self._vector.get_column_color())

            geojson = json.loads(feature.geometry().exportToGeoJSON())
            geom_type = geojson[self.TYPE_JSON]
            coordinates = geojson[self.COORDINATES_JSON]
            if self._is_multi(geom_type):
                # Multi part geom
                for geometry in coordinates:
                    d[self.COORDINATES_JSON] = self._read_geometry(geometry, geom_type)
                    ret_tile.append(d)
            else:
                # Simple part geom
                d[self.COORDINATES_JSON] = self._read_geometry(coordinates, geom_type)
                ret_tile.append(d)
        return ret_tile

    ##  _read_geometry method
    #   TODO
    #   @param array
    #   @param geometry_type
    #   @return an array
    def _read_geometry(self, array, geometry_type):
        coord = []
        if self._is_point(geometry_type):
            return self._read_point(array, coord)
        elif self._is_line(geometry_type):
            for point in array:
                coord = self._read_point(point, coord)
            return coord
        elif self._is_polygon(geometry_type):
            for line in array:
                for point in line:
                    coord = self._read_point(point, coord)
            return coord
        else:
            self.logger.error("Unexpected geometry type " + geometry_type)

    ##  _read_point method
    #   TODO
    #   @param array_in
    #   @param array_out
    #   @return an array
    def _read_point(self, array_in, array_out):
        out = array_out
        # Add X
        out.append(array_in[0])
        # Add Y
        out.append(array_in[1])
        return out

    ##  _is_multi method
    #   TODO
    #   @param gtype
    #   @return boolean
    def _is_multi(self, gtype):
        return gtype.startswith(self.MULTI)

    ##  _is_point method
    #   TODO
    #   @param gtype
    #   @return boolean
    def _is_point(self, gtype):
        return gtype == self.POINT_1 or gtype == self.POINT_2

    ##  _is_line method
    #   TODO
    #   @param gtype
    #   @return boolean
    def _is_line(self, gtype):
        return gtype == self.LINE_1 or gtype == self.LINE_2

    ##  _is_polygon method
    #   TODO
    #   @param gtype
    #   @return boolean
    def _is_polygon(self, gtype):
        return gtype == self.POLYGON_1 or gtype == self.POLYGON_2

    ##  _can_convert method
    #   TODO
    #   @return boolean
    def _can_convert(self):
        if self._vector._dimension is None:
            self.logger.warning("Dimension is None")
            return False
        if self._vector._geometry is None:
            self.logger.warning("Geometry is None")
            return False
        if self._vector._color._colors is None:
            self.logger.warning("Colors is None")
            return False
        return True
