import logging


##  Converter Class
class Converter:

    DIM = "dim"
    COLOR = "color"
    TYPE = "type"
    UUID = "uuid"
    GEOMETRIES = "geometries"
    FEATURE = "feature"

    ## Constructor
    def __init__(self):
        self.logger = logging.getLogger('Vizitown')

    ## convert method
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
    # INPUT DATA AN ARRAY OF DICTIONARY
    # [
    #     {
    #         'color': '#f7fbff',
    #         'feature': [{'coordinates': [646084.5135765221, 6859254.556517816], 'height': '0'}]
    #     },
    #     {
    #         'color': '#e6f0f9',
    #         'feature': [
    #             {'coordinates': [646246.4825060187, 6859419.074442579], 'height': '0'},
    #             {'coordinates': [646186.253073064, 6859059.939874367], 'height': '0'}
    #         ]
    #     }
    # ]
    #   TODO
    #   @param data
    #   @param geometry
    #   @param dim
    #   @param uuid
    #   @return an array
    def convert(self, data, geometry, dim, uuid):
        if (data is None or
                geometry is None or
                dim is None or
                uuid is None):
            self.logger.error("Can't convert data missing some information")

        dictionary = {}
        dictionary[self.DIM] = dim
        dictionary[self.TYPE] = geometry
        dictionary[self.UUID] = uuid

        array = []

        for d in data:
            tmp = dictionary
            tmp[self.COLOR] = d[self.COLOR]
            geometries = d[self.FEATURE]
            if len(geometries) != 0:
                tmp[self.GEOMETRIES] = d[self.FEATURE]
                array.append(dict(tmp))

        return array
