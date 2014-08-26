from qgis.core import *

from .. import core


class Color:
    SINGLE = "singleSymbol"
    GRADUATE = "graduatedSymbol"
    CATEGORIZED = "categorizedSymbol"

    ##  Color constructor
    #   @param rendererV2 renderer link with a QgsMapLayer
    def __init__(self, renderer):
        self.logger = core.Logger.instance()
        self._renderer = renderer

        #   Color type : singleSymbol, graduateSymbol, categorizedSymbol
        self._type = renderer.type()

        #   Array use to define symbol contains dictionary
        #   Different kind of dictionary according to color type
        #   singleSymbol -> {'color': String(#000000)}
        #   graduateSymbol -> {'min': int, 'max': int, 'color': String(#000000)}
        #   categorizedSymbol -> {'value': , 'color': String(#000000)}
        self._colors = []
        self._define_color()

    ##  Sort data according to symbol
    #   @param data ??
    #   @return ??
    def sort_result(self, data):
        # I'm waiting to see what data can i get
        raise NotImplementedError, "TO DO"

    ##  
    #   If user change color in QGIS an event is triggered so the renderer change
    #   and all values of color Class in same time
    #   @param rendererV2 renderer link with a QgsMapLayer
    def update(self, renderer):
        self._renderer = renderer
        self._type = renderer.type()
        self._define_color()

    ##  Define all useful informations to sort vector data
    def _define_color(self):
        tabColor = []
        color = []
        size = 0

        if self._type == self.SINGLE:
            tabColor.append({'color': str(self._renderer.symbol().color().name())})

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
                tabColor.append({'min': lowerValue[i], 'max': upperValue[i], 'color': color[i]})

        elif self._type == self.CATEGORIZED:
            value = []

            for symbol in self._renderer.symbols():
                color.append(str(symbol.color().name()))
                size = size + 1
            for categorie in self._renderer.categories():
                value.append(categorie.value())
            for i in xrange(size):
                tabColor.append({'value': value[i], 'color': color[i]})

        else:
            self.logger.warning("core/Color - Symbol type unhandled")
            #raise ValueError, "Symbol type unhandled"

        self._colors = tabColor