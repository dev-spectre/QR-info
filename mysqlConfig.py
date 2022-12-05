import sql
import website
import mysql.connector as mysql


def setup_database(user = "root"):
    password = sql.get_pass()
    
    conn = mysql.connect(
        host = "localhost",
        user = user,
        password = password
        )
    cursor = conn.cursor()

    database = "qrinfo"
    try:
        cursor.execute(f"CREATE DATABASE {database}")
    except mysql.errors.DatabaseError:
        pass
    finally:
        cursor.execute(f"USE {database}")

    try:
        cursor.execute(
            """CREATE TABLE website_info(
                domain VARCHAR(255) PRIMARY KEY,
                info VARCHAR(15000) NOT NULL,
                added_by CHAR(5) NOT NULL
            )"""
        )
    except mysql.errors.ProgrammingError:
        pass
    finally:
        file = open("./info.txt")
        for line in file:
            rec = eval(line)
            domain = website.extract_domain(rec[0])
            info = rec[1].strip()
            try:
                cursor.execute(
                    f"""INSERT INTO website_info(domain, info, added_by)
                        VALUES ("{domain}", "{info}", "ADMIN")
                    """
                )
            except mysql.errors.IntegrityError:
                pass

        file.close()
        
    conn.commit()
    conn.close()

password = sql.get_pass()

try:
    with sql.connect_to_database(password) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(added_by) FROM website_info WHERE added_by = 'ADMIN'")
        result = cursor.fetchone()
        if result[0] != 83:
            setup_database(user = "root")

except mysql.errors.ProgrammingError:
    setup_database(user = "root")
