import logging

from color import Color


class Vector:

    GEOMETRY = "geometry"

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
        # Have to be improve
        self._uuid = self._display_name

    def update_color(self):
        renderer = self._qgisLayer.rendererV2()
        self._color.update(renderer)

    def get_renderer(self):
        return self._qgisLayer.rendererV2()

    def has_column_color(self):
        if self._color._column_color is not None:
            return True
        return False

    def get_column_color(self):
        return self._color._column_color

    def define_column2(self, name, type):
        self._has_2_column = True
        self._column2_name = name
        self._column2_type = type
        if type == self.GEOMETRY:
            self._column2_is_geom = True
        self.define_dimension()

    def define_dimension(self):
        if not self._has_2_column:
            self._dimension = 2
        else:
            if self._column2_is_geom:
                self._dimension = 3
            else:
                self._dimension = 2.5