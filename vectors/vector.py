import uuid
import logging

from color import Color


##  Vector class
#   TODO
class Vector:

    GEOMETRY = "geometry"

    POINT = "point"
    LINE = "line"
    POLYGON = "polygon"

    ##  Constructor
    def __init__(self, QgsMapLayer):
        self.logger = logging.getLogger('Vizitown')
        self._qgisLayer = QgsMapLayer

        self._has_2_column = False
        self._column2_name = None
        self._column2_is_geom = False
        self._column2_type = None

        self._display_name = QgsMapLayer.name()

        self._color = Color(QgsMapLayer.rendererV2())

        # Data for browser
        self._geometry = None
        self._dimension = None
        self._uuid = str(uuid.uuid1())

    ##  update_color method
    #   TODO
    def update_color(self):
        renderer = self._qgisLayer.rendererV2()
        self._color.update(renderer)
        self.define_dimension()

    ##  get_renderer method
    #   TODO
    def get_renderer(self):
        return self._qgisLayer.rendererV2()

    ##  has_column_color method
    #   TODO
    def has_column_color(self):
        if self._color._column_color is not None:
            return True
        return False

    ##  get_column_color method
    #   TOOD
    def get_column_color(self):
        return self._color._column_color

    ##  define_column2 method
    #   TODO
    def define_column2(self, name, type):
        self._has_2_column = True
        self._column2_name = name
        self._column2_type = type
        if type == self.GEOMETRY:
            self._column2_is_geom = True
        self.define_dimension()

    ##  define_dimension method
    #   TODO
    def define_dimension(self):
        if self._has_2_column:
            if self._column2_is_geom:
                self._dimension = "3"
            else:
                self._dimension = "2.5"
        else:
            self._dimension = "2"

    ## define_geometry method
    #   TODO
    #   @param gtype
    def define_geometry(self, gtype=None):
        if gtype is not None:
            self._geometry = gtype
        else:
            nbtype = self._qgisLayer.geometryType()
            if nbtype == 0:
                self._geometry = self.POINT
            elif nbtype == 1:
                self._geometry = self.LINE
            elif nbtype == 2:
                self._geometry = self.POLYGON
            else:
                self.logger.error("Unexpected number of geometry type -> " + nbtype)
