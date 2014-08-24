from color import Color


class Vector:

    def __init__(self, QgsMapLayer):
        self._qgisLayer = QgsMapLayer
        # self._provider = Provider

        self._column2_name = None
        self._column2_type = None

        self._displayName = QgsMapLayer.name()
        # Have to be improve
        self._uuid = self._displayName

        self._color = Color(QgsMapLayer.rendererV2())