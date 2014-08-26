from vector import Vector
from postgis_provider import PostgisProvider
from shapefile_provider import ShapefileProvider
from .. import core


class VectorProviderFactory:
    SHAPEFILE = "ESRI Shapefile"
    POSTGIS = "PostgreSQL database with PostGIS extension"

    def __init__(self):
        self.logger = core.Logger.instance()
    
    def create_provider(self, QgsMapLayer):
        vector = Vector(QgsMapLayer)
        storageType = QgsMapLayer.storageType()
        provider = None

        if storageType == self.SHAPEFILE:
            provider = ShapefileProvider(vector)
        elif storageType == self.POSTGIS:
            provider = PostgisProvider(vector)
        else:
            self.logger.warning("Vector data type unhandled")

        return provider