import re


## parseVector to recuperate vector information in QGIS
#  This function give the query to ask the database and
#  return vectors informations into QGIS
#  @param source String information to query the database
#  @param srid of the vector layer
#  @param color of the vector layer
#  @return String with vectors informations
def parse_vector(source, srid, color):
    m = re.match(r"""
    \s*dbname='(?P<dbname>.*?)'\s*host=(?P<host>\d+.\d+.\d+.\d+)\s*port=(?P<port>\d+)
    \s*user='(?P<user>.*?)'\s*password='(?P<password>.*?)'\s*.*
    \s*.*\s*table=(?P<table>\S+)\s*\((?P<column>.*?)\)""", source, re.X)
    return {
        'dbname': m.group('dbname'),
        'host': m.group('host'),
        'port': int(m.group('port')),
        'user': m.group('user'),
        'password': m.group('password'),
        'srid': srid,
        'table': m.group('table'),
        'column': m.group('column'),
        'color': color
    }
