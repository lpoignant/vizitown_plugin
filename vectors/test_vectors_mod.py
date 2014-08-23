import unittest

from postgis_provider import PostgisProvider
from vector import Vector


class MockQgsMapLayer:

    def __init__(self):
        self._source = ("dbname='vizitown' host=127.0.0.1 "
                        "port=5432 user='postgres' password='postgres' "
                        "sslmode=disable key='gid' srid=3857 type=POINT "
                        "table=\"public\".\"sbc_airports_3857\" (geom) sql=")

    def source(self):
        return self._source


class TestVectorsModuleParsingPostgisSource(unittest.TestCase):

    def setUp(self):
        mqml = MockQgsMapLayer()
        v = Vector(mqml)
        self.pg_provider = PostgisProvider(v)

    def test_dbname(self):
        dbname = "vizitown"
        self.assertEqual(self.pg_provider._dbname, dbname)

    def test_host(self):
        host = "127.0.0.1"
        self.assertEqual(self.pg_provider._host, host)

    def test_port(self):
        port = 5432
        self.assertEqual(self.pg_provider._port, port)

    def test_user(self):
        user = "postgres"
        self.assertEqual(self.pg_provider._user, user)

    def test_password(self):
        password = "postgres"
        self.assertEqual(self.pg_provider._password, password)

    def test_table(self):
        table = "\"public\".\"sbc_airports_3857\""
        self.assertEqual(self.pg_provider._table, table)

    def test_column(self):
        column = "geom"
        self.assertEqual(self.pg_provider._column, column)

if __name__ == '__main__':
    test1 = unittest.TestLoader().loadTestsFromTestCase(TestVectorsModuleParsingPostgisSource)
    test2 = unittest.TestLoader().loadTestsFromTestCase(TestVectorsModuleParsingPostgisSource)
    unittest.TextTestRunner(verbosity=2).run(test1)
    unittest.TextTestRunner(verbosity=2).run(test2)