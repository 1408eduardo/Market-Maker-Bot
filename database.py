import sqlite3

class Database:
    def __init__(self, db_app):
        self.conn = sqlite3.connect(db_app)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """Create a table in the database"""
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, ', '.join(columns))
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        """Insert data into a table"""
        query = "INSERT INTO {} VALUES ({})".format(table_name, ', '.join(['?'] * len(data)))
        self.cursor.execute(query, data)
        self.conn.commit()

    def retrieve_data(self, table_name, columns, conditions):
        """Retrieve data from a table"""
        query = "SELECT {} FROM {} WHERE {}".format(', '.join(columns), table_name, conditions)
        self.cursor.execute(query)
        return self.cursor.fetchall
