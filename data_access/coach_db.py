import sqlite3
from typing import List, Dict

class CoachDB:
    def __init__(self, db_path: str = "coach.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS pokemon (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    height INTEGER,
                    weight INTEGER,
                    types TEXT,
                    abilities TEXT
                )
            """)
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    height INTEGER,
                    weight INTEGER,
                    types TEXT,
                    abilities TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def save_pokemon(self, pokemon: Dict):
        with self.connection:
            self.connection.execute("""
                INSERT INTO pokemon (name, height, weight, types, abilities)
                VALUES (:name, :height, :weight, :types, :abilities)
            """, pokemon)

    def save_history(self, pokemon: Dict):
        with self.connection:
            self.connection.execute("""
                INSERT INTO history (name, height, weight, types, abilities)
                VALUES (:name, :height, :weight, :types, :abilities)
            """, pokemon)

    def get_saved_pokemon(self) -> List[Dict]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pokemon")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def get_history(self) -> List[Dict]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
