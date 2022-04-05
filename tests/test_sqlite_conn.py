from sqlite_conn import SQLiteConn

def test_create_show_table():
    with SQLiteConn('test.db') as test_conn:
        test_conn.cursor.execute("DROP table IF EXISTS Shows;")
        test_conn.create_shows_table()
        test_conn.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        assert test_conn.cursor.fetchall() == [('Shows',)]

def test_write_rows_to_shows_table():
    with SQLiteConn('test.db') as test_conn:
        test_conn.cursor.execute("DELETE FROM Shows;")
        test_conn.write_rows_to_shows_table([('123','Random','ja',8.87),('234','Random again','en',9.99)])
        test_conn.cursor.execute("SELECT COUNT(*) FROM Shows;")
        assert test_conn.cursor.fetchall() == [(2,)]
