import sqlite3

class Database:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("""INSERT into users (user_id) VALUES (?)""", (user_id,))
            self.connection.commit()

    def user_exists(self, user_id):
        with self.connection:
            res = self.cursor.execute("""SELECT * from users WHERE user_id = ?""", (user_id,)).fetchall()
            return bool(len(res))

    def all_users(self):
        with self.connection:
            return self.cursor.execute("""SELECT * from users""").fetchall()

    def count_users(self):
        with self.connection:
            return self.cursor.execute("""SELECT count (*) FROM users""").fetchall()

    def set_ban(self, user_id):
        with self.connection:
            self.cursor.execute("""UPDATE user SET banned = 1 WHERE user_id = ?""", (user_id,))
            self.connection.commit()

    def check_ban(self, user_id):
        with self.connection:
            return self.cursor.execute("""SELECT banned FROM users WHERE user_id = ?""", (user_id,)).fetchone()

    def add_count(self, user_id):
        with self.connection:
            self.cursor.execute("""UPDATE users SET count_gens = count_gens + 1 WHERE user_id = ?""", (user_id,))
            self.connection.commit()

    def add_all_count(self):
        with self.connection:
            self.cursor.execute("""UPDATE stats SET created_all = created_all + 1""")
            self.connection.commit()

    def add_today(self):
        with self.connection:
            self.cursor.execute("""UPDATE stats SET created_today = created_today + 1""")
            self.connection.commit()

    def update_date(self, date):
        with self.connection:
            self.cursor.execute("""UPDATE stats SET day = ?""", (date,))
            self.connection.commit()

    def refresh_data(self):
        with self.connection:
            self.cursor.execute("""UPDATE stats SET created_today = 0""")
            self.connection.commit()

    def stats(self):
        with self.connection:
            return self.cursor.execute("""SELECT * from stats""").fetchone()

    def user_stats(self, user_id):
        with self.connection:
            return self.cursor.execute("""SELECT * from users WHERE user_id = ?""", (user_id,)).fetchone()
