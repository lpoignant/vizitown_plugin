import re
from vector_provider import VectorProvider

from PyQt4.QtSql import *


class ShapefileProvider(VectorProvider):

    def __init__(self, vector):
        VectorProvider.__init__(self, vector)