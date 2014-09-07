import logging

from vector_provider import VectorProvider


##	ShapefileProvider class
class ShapefileProvider(VectorProvider):

    ## Constructor
    def __init__(self, vector):
        VectorProvider.__init__(self, vector)
        self.logger = logging.getLogger('Vizitown')
