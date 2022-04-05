import sqlite3
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def sqlite_exception_handle(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except sqlite3.Error as e:
            raise e
    return decorated

class SQLiteConn(object):
    
    def __init__(self, name=None):        
        self.conn = None
        self.cursor = None
        if name:
            self.open(name)
    
    @sqlite_exception_handle
    def open(self,name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
    
    def close(self):        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):        
        return self

    def __exit__(self, exc_type,exc_value, exc_traceback):        
        self.close()

    @sqlite_exception_handle            
    def write_rows_to_shows_table(self,data):        
        query = "INSERT INTO Shows (id,name,original_language,vote_average) VALUES (?,?,?,?);"
        self.cursor.executemany(query,data)
        self.conn.commit()

    @sqlite_exception_handle
    def create_shows_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
               (id TEXT, name TEXT, original_language TEXT, vote_average REAL)''')
        self.conn.commit()

if __name__ == '__main__':
    with SQLiteConn('test.db') as myconn:
        myconn.create_shows_table()
        data = [(1,2,3,4),(2,3,4,5,6)]
        myconn.write_rows_to_shows_table(data)
