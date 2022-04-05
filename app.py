# 1. get data from API
# 2. write to SQLite
from tmdbwrapper import TV
from sqlite_conn import SQLiteConn
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_popular_tv_by_page(tv,page):
    logger.info(f'retrieving page {page} result from TMDB')
    return tv.popular(page)

def write_data_to_sqlite(conn, data):
    logger.info(f"writing {len(data)} rows to Shows table")
    conn.write_rows_to_shows_table(data)


def main():
    mytv = TV()
    page = 1
    with SQLiteConn('tv_shows.db') as myconn:
        myconn.create_shows_table()
        while True:
            data = get_popular_tv_by_page(mytv,page)
            print(data)
            if data and page <= 10:
                write_data_to_sqlite(myconn,data)
                page += 1
            else:
                break

if __name__ == '__main__':
    main()