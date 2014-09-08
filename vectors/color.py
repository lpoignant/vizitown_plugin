import logging

from qgis.core import *


##  Color Class
#   TODO
class Color:
    SINGLE = "singleSymbol"
    GRADUATE = "graduatedSymbol"
    CATEGORIZED = "categorizedSymbol"

    HEIGHT = "height"
    DATA = "data"
    COORDINATES_JSON = "coordinates"

    MIN = "min"
    MAX = "max"
    VALUE = "value"

    COLOR = "color"
    FEATURE = "feature"

    ##  Color constructor
    #   @param rendererV2 renderer link with a QgsMapLayer
    def __init__(self, renderer):
        self.logger = logging.getLogger('Vizitown')
        self._renderer = renderer

        #   Color type : singleSymbol, graduateSymbol, categorizedSymbol
        self._type = renderer.type()

        #   Array use to define symbol contains dictionary
        #   Different kind of dictionary according to color type
        #   singleSymbol -> {'color': String(#000000)}
        #   graduateSymbol -> {'min': int, 'max': int, 'color': String(#000000)}
        #   categorizedSymbol -> {'value': , 'color': String(#000000)}
        self._colors = None
        self._column_color = None

        self._define_color()

    ##  Sort data according to symbol
    #   @param data ??
    #   @return ??
    def sort_result(self, data):
        # I'm waiting to see what data can i get
        if self._type == self.SINGLE:
            sort_data = self._sort_single(data)
        elif self._type == self.GRADUATE:
            sort_data = self._sort_graduated(data)
        elif self._type == self.CATEGORIZED:
            sort_data = self._sort_categorized(data)
        else:
            self.logger.error("Unexpected data type")

        return self._associate_color(sort_data)

    ## _sort_single method
    #  TODO
    #  @param feature_array
    #  @return an array
    def _sort_single(self, feature_array):
        nbColor = len(self._colors)
        array = [[] for i in range(nbColor)]

        for feature in feature_array:
            for i in range(nbColor):
                array[i].append(feature)
        return array

    ## _sort_graduated method
    #  TODO
    #  @param feature_array
    #  @return an array
    def _sort_graduated(self, feature_array):
        nbColor = len(self._colors)
        array = [[] for i in range(nbColor)]

        for feature in feature_array:
            for i in range(nbColor):
                # print feature
                if not self.DATA in feature.keys():
                    break
                data = feature[self.DATA]

                if (data >= self._colors[i][self.MIN] and
                        data <= self._colors[i][self.MAX]):
                    del feature[self.DATA]
                    array[i].append(feature)
                    break
        return array

    ## _sort_categorized method
    #  TODO
    #  @param feature_array
    #  @return an array
    def _sort_categorized(self, feature_array):
        nbColor = len(self._colors)
        array = [[] for i in range(nbColor)]

        for feature in feature_array:
            for i in range(nbColor):
                # print feature
                if not self.DATA in feature.keys():
                    break
                if (feature[self.DATA]).encode('utf-8') == (self._colors[i][self.VALUE]).encode('utf-8'):
                    del feature[self.DATA]
                    array[i].append(feature)
                    break
        return array

    ##  _associate_color method
    #   TODO
    #   @param array
    #   @return an array
    def _associate_color(self, array):
        ret = []
        for i in range(len(self._colors)):
            d = {self.COLOR: self._colors[i][self.COLOR]}
            d[self.FEATURE] = array[i]
            ret.append(d)
        return ret

    ##  update method
    #   If user change color in QGIS an event is triggered so the renderer change
    #   and all values of color Class in same time
    #   @param rendererV2 renderer link with a QgsMapLayer
    def update(self, renderer):
        self._renderer = renderer
        self._type = renderer.type()
        self._define_color()

    ##  _define_color method
    #   Define all useful informations to sort vector data
    def _define_color(self):
        tabColor = []
        color = []
        size = 0

        if self._type == self.SINGLE:
            tabColor.append({self.COLOR: str(self._renderer.symbol().color().name())})

        elif self._type == self.GRADUATE:
            lowerValue = []
            upperValue = []

            for symbol in self._renderer.symbols():
                color.append(str(symbol.color().name()))
                size = size + 1
            for _range in self._renderer.ranges():
                lowerValue.append(_range.lowerValue())
                upperValue.append(_range.upperValue())
            for i in xrange(size):
                tabColor.append({self.MIN: lowerValue[i], self.MAX: upperValue[i], self.COLOR: color[i]})

        elif self._type == self.CATEGORIZED:
            value = []

            for symbol in self._renderer.symbols():
                color.append(str(symbol.color().name()))
                size = size + 1
            for categorie in self._renderer.categories():
                value.append(categorie.value())
            for i in xrange(size):
                tabColor.append({self.VALUE: value[i], self.COLOR: color[i]})

        else:
            self.logger.error("Symbol type unhandled")

        self._column_color = self.get_column_color()
        self._colors = tabColor

    ## get_column_color method
    #  Get the name of the column where the analysis was perform. If there isn't analysis, the name is none
    #  @return the color column
    def get_column_color(self):
        if self._type == self.SINGLE:
            return None
        if self._type == self.GRADUATE or self._type == self.CATEGORIZED:
            return self._renderer.classAttribute()
