

class VectorProvider:

    def __init__(self, vector):
        self._vector = vector

    ## get_column_info metho
    # Gives all data column name + data type
    # @return A dict such as {attribute name: attribute type}
    def get_columns_info(self):
        attributes = self._vector._qgisLayer.pendingFields().toList()
        result = {}
        for a in attributes:
            result[a.name()] = a.typeName()
        return result

    def add_column2(self, name, type):
        self._vector._column2_name = name
        self._vector._column2_type = type

    def request_tile(self, tile):
        raise NotImplementedError