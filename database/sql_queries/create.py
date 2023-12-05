CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    id_user INTEGER UNIQUE,
    email TEXT,
    password TEXT
)
"""
