from database.sql_lite_db import SQLiteDB
from database.sql_queries.create import CREATE_TABLE_USERS
from database.sql_queries.delete import DELETE_USER
from database.sql_queries.insert import USER_INSERT


class DataBaseManager(SQLiteDB):
    def create_table_user(self):
        self.execute_data(CREATE_TABLE_USERS)

    def insert_user(self, id_user: int, email: str, password: str):
        user = USER_INSERT.format(
            id_user=id_user,
            email=email,
            password=password,
        )
        self.execute_data(user)

    def delete_user(self, id_user):
        user = DELETE_USER.format(
            id_user=id_user,
        )
        self.execute_data(user)
