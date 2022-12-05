import mysql.connector as mysql

password = ""

def get_pass():
    global password
    
    if password != "":
        return password
    
    file = open("./pass.txt")
    data = file.read()
    for char in data:
        if char != '\n':
            password += char
    file.close()
    
    if password == "":
        password = input("MySQL password: ")
        
    return password

def connect_to_database(password):
    try:
        conn = mysql.connect(
                host = "localhost",
                user = "root",
                password = password,
                database = "qrinfo"
                )
    except mysql.errors.ProgrammingError:
        print("Invalid password for user root\n")
        password = input("MySQL password: ")
        conn = connect_to_database(password)
    return conn

def get_info(url):
    password = get_pass()
    with connect_to_database(password) as conn:
        cursor = conn.cursor()
        run = cursor.execute
        run(f"SELECT info, added_by FROM website_info WHERE domain = '{url}'")
        result = cursor.fetchone()
    return result

def format_info(data):
    formated_data = ""
    if data is None:
        return
    for char in data:
        if char != '"':
            formated_data += char
        else:
            formated_data += "'"
    return formated_data

def add_to_database(domain, website_info):
    password = get_pass()
    with connect_to_database(password) as conn:
        cursor = conn.cursor()
        website_info #Don't remove this line, this is intentional
        formated_info = format_info(website_info)
        try:
            cursor.execute(f'INSERT INTO website_info(domain, info, added_by) VALUES("{domain}", "{formated_info}", "USER")')
        except mysql.errors.IntegrityError:
            cursor.execute(f'UPDATE website_info SET info = "{formated_info}" WHERE domain = "{domain}" AND added_by = "USER"')
        conn.commit()
