import logging

from vector import Vector
from postgis_provider import PostgisProvider
from shapefile_provider import ShapefileProvider


class VectorProviderFactory:
    SHAPEFILE = "ESRI Shapefile"
    POSTGIS = "PostgreSQL database with PostGIS extension"

    def __init__(self):
        self.logger = logging.getLogger('Vizitown')
    
    def create_provider(self, QgsMapLayer):
        vector = Vector(QgsMapLayer)
        storageType = QgsMapLayer.storageType()
        provider = None

        if storageType == self.SHAPEFILE:
            provider = ShapefileProvider(vector)
        elif storageType == self.POSTGIS:
            provider = PostgisProvider(vector)
        else:
            self.logger.warning("core/factory_vector_provider - Vector data type unhandled")

        return provider