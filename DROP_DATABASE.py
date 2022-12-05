import setup
import sql
import mysql.connector as mysql

if __name__ == "__main__":

    password = sql.get_pass()

    try:
        conn = sql.connect_to_database(password)
        cursor = conn.cursor()
        database = input("TYPE 'qrinfo' TO DELETE DATABASE: ")
        if database == "qrinfo":
            cursor.execute(f"DROP DATABASE {database}")
            conn.commit()
            conn.close()
            print("DATABASE DELETED")
        else:
            print("DATABASE NOT DELETED")

    except mysql.errors.ProgrammingError:
        print("DATABASE qrinfo DOESN'T EXIST")
