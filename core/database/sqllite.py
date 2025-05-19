import sqlite3


class DB:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        print("База подключена")

        self.cursor.execute("DROP TABLE IF EXISTS Message")

        self.connection.commit()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Message(
                id INTEGER PRIMARY KEY,
                client_address TEXT NOT NULL,
                data TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def save_message(self, client_address, message):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO Message(client_address, data) VALUES (?, ?)",
                (client_address, message),
            )

    def get_message_list_by_address(self, client_address):
        self.cursor.execute(
            f"SELECT data FROM Message WHERE client_address = '{client_address}'"
        )
        all_messages_from_db = self.cursor.fetchall()
        return_data = []
        for message in all_messages_from_db:
            return_data.append(message[0])

        return return_data
