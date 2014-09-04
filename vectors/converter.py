import logging


class Converter:

    def __init__(self):
        self.logger = logging.getLogger('Vizitown')


    # Have to return something like that :
    # {
    # "dim"          : "2.5",
    # "color"        : "#926ae7",
    # "type"         : "polygon",
    # "uuid"         : "geopublic.batiment_polygon_simplegeom",
    # "geometries"   : [
    #     {
    #         "height"        : 7,
    #         "coordinates"   : [X1, Y1, X2, Y2]
    #     }]
    # }

    # Receive dict such as
    # {
    #   "height": X 0 if no height
    #   "coordinates" : [] array of coordinates in 2 dimensions only X and Y
    #   "data" : X data to sort
    # }
    def convert(self, dict):
        return None