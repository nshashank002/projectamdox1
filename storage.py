import sqlite3

def save_to_db(data):
    conn = sqlite3.connect("crypto.db")
    data.to_sql("crypto_data", conn, if_exists="replace", index=False)
    conn.close()
