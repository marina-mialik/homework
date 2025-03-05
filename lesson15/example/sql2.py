import sqlite3

class SQLiteConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def execute(self, query, params=None):
        
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()

# Пример использования
with SQLiteConnection('lesson15\\example\\test2.db') as db:
    db.execute("SELECT * FROM users")
    records = db.fetch_all()
    for record in records:
        print(record)