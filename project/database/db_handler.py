# import sqlite3


# def init_database():
#     conn = sqlite3.connect("camera_app.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS actions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             action TEXT,
#             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#         )
#     """
#     )
#     conn.commit()
#     conn.close()


# def log_action(action):
#     conn = sqlite3.connect("camera_app.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO actions (action) VALUES (?)", (action,))
#     conn.commit()
#     conn.close()
