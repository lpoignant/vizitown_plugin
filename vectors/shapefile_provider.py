import re

from PyQt4.QtSql import *

import core

from vector_provider import VectorProvider


class ShapefileProvider(VectorProvider):

    def __init__(self, vector):
        VectorProvider.__init__(self, vector)