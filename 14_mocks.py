import unittest
from unittest.mock import Mock
from requests.exceptions import Timeout

cx_Oracle = Mock()

def query_database(sql):
    
    db_user = "blah"
    db_pass = "blah"
    db_dsn = '(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = tcp)(host = host1) (Port = 1525))) (CONNECT_DATA = (SID = orcl)))'

    try:
        res = cx_Oracle.connect(db_user, db_pass, dsn=db_dsn).cursor().execute(sql).fetchall()
        print("Query executed successfully.")
    except:
        print("Insert the error into a log table.")

    return res[0][0]

class TestDatabase(unittest.TestCase):
    def test1_query_database(self):
        sql = "select max(id) from orders"
        cx_Oracle.connect().cursor().execute(sql).fetchall.return_value = [(100,)]
        self.assertEqual(query_database(sql), 100)

    def test2_query_database(self):
        sql = "select max(id) from orders"
        cx_Oracle.connect().cursor().execute(sql).fetchall.side_effect = [[(100,)], Timeout]
        self.assertEqual(query_database(sql), 100)
        with self.assertRaises(Exception):
            query_database(sql)

if __name__ == '__main__':
    unittest.main()
