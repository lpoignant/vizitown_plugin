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

        self._displayName = QgsMapLayer.name()
        # Have to be improve
        self._uuid = self._displayName

        self._color = Color(QgsMapLayer.rendererV2())

    def update_color(self):
        renderer = self._qgisLayer.rendererV2()
        self._color.update(renderer)

    def get_renderer(self):
        return self._qgisLayer.rendererV2()

    def define_column2(self, name, type):
        self._has_2_column = True
        self._column2_name = name
        self._column2_type = type
        if type == self.GEOMETRY:
            self._column2_is_geom = True
        self.logger.debug("core/vector - _has_2_column -> " + str(self._has_2_column))
        self.logger.debug("core/vector - _column2_name -> " + self._column2_name)
        self.logger.debug("core/vector - _column2_type -> " + self._column2_type)
        self.logger.debug("core/vector - _column2_is_geom -> " + str(self._column2_is_geom))