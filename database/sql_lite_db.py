import sqlite3

from utils.logger import logger


class SQLiteDB:
    path_db = 'database/user.db'
    _instance = None

    def __new__(cls, db_name=path_db):
        if cls._instance is None:
            logger.debug("create new connect SQLiteDB")
            cls._instance = super(SQLiteDB, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def create_table(self, query):
        logger.debug(query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, query):
        logger.debug(f"query - {query}")
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query):
        logger.debug(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        logger.debug("close connect")
        self.conn.close()

    def __del__(self):
        logger.debug("close connect")
        self.conn.close()
