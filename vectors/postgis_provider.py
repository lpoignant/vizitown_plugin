import re

from PyQt4.QtSql import *

from .. import core

from vector_provider import VectorProvider

class PostgisProvider(VectorProvider):

    def __init__(self, vector):
        VectorProvider.__init__(self, vector)
        self.logger = core.Logger.instance()

        self._dbname    = None
        self._host      = None
        self._port      = None
        self._user      = None
        self._password  = None
        self._table     = None
        self._column    = None

        self._db        = None

        #   Define SRID UNUSE right now
        #VectorProvider._vector._srid = self._vector._qgisLayer.crs().postgisSrid()

        #   Define above variables
        self._parse_source()
        #   Define self._db use for sql request
        self.__define_database()

    def request_tile(self, tile):
        self._vector.update_color()
        core.Logger.instance().debug("Request Tile Postgis Provider")
        if not self._vector._has_2_column:
            VectorProvider.request_tile(self, tile)
        else:
            self.logger.error("NOT IMPLEMENTED YET - TODO")
        raise NotImplementedError

    ## _parse_source method
    #  Parse QgsMapLayer.source() (String) to save useful data
    #  in order to request database
    def _parse_source(self):
        source = self._vector._qgisLayer.source()
        dbname = re.match(r".*dbname='(\S+)'", source)
        self._dbname = dbname.group(1)

        host = re.match(r".*host=(\S+)", source)
        self._host = host.group(1)

        port = re.match(r".*port=(\d+)", source)
        self._port = int(port.group(1))

        # User could be optional
        user = re.match(r".*user='(\S+)'", source)
        if not user:
            self._user = ""
        else:
            self._user = user.group(1)

        # Password could be optional
        password = re.match(r".*password='(\S+)'", source)
        if not password:
            self._password = ""
        else:
            self._password = password.group(1)

        # Contains schema + table
        table = re.match(r".*table=(\S+)", source)
        self._table = table.group(1)

        column = re.match(r".*\((\S+)\)", source)
        self._column = column.group(1)

        self._vector._uuid = re.sub("\"", "", str(self._dbname + self._table + self._column))

    ##  _define_database method
    #   write comment
    def __define_database(self):
        self._db = QSqlDatabase.addDatabase("QPSQL", self._vector._uuid)
        self._db.setHostName(self._host)
        self._db.setDatabaseName(self._dbname)
        self._db.setPort(self._port)
        self._db.setUserName(self._user)
        self._db.setPassword(self._password)
        core.Logger.instance().info("Database define")

    def _open_connection(self):
        if not self._db.open():
            self.logger.error("core/postgis_provider - Connection to database cannot be established")
            raise Exception('Connection to database cannot be established')
        self.logger.info("core/postgis_provider - Connection to db established")


    def _close_connection(self):
        self._db.close()
        core.Logger.instance().info("core/postgis_provider - Connection to db closed")