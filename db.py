import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sat95",
        database="cafeverse"
    )
    return connection

if __name__ == "__main__":
    try:
        conn = connect_db()
        print("✅ Database Connected Successfully!")
        conn.close()
    except Exception as e:
        print(e)