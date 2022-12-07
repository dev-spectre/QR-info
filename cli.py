import website
import sql
import qr
import os
import tkinter, tkinter.filedialog

def get_file_path():
    win = tkinter.Tk()
    win.withdraw()
    win.attributes("-topmost", True)
    file_path = tkinter.filedialog.askopenfilename(parent = win)
    return file_path

def get_file(file_path):
    file_name = os.path.basename(file_path)
    if os.path.splitext(file_name)[1] in [".png", ".jpg", ".jpeg"]:
        return file_name

def display_selected_file(file_path):
    file_name = get_file(file_path)
    if file_name:
        print()
        print("Selected file:", file_name, end = "\n\n\n")
    else:
        print("Invalid file format")
        print("Supported formats are png, jpg and jpeg", end = "\n\n")

def scan_qr():
    file_path = get_file_path()
    if not file_path:
        return
    display_selected_file(file_path)
    data = qr.get_data(file_path)
    return data

def is_url(string):
    if string.startswith("https://") or string.startswith("http://"):
        return True
    return False

def get_site_info(url):
    domain = website.extract_domain(url)
    site_info = sql.get_info(domain)
    if site_info:
        return domain, site_info[0], True
    short_url = website.get_short_url(url)
    site_info = website.get_info_from_ai(short_url)
    return domain, site_info, False

def add_data_to_database(domain, site_info, from_database):
    if from_database:
        return
    while True:
        print()
        choice = input("Do you want to enter site info to database (y/n): ")
        if choice in ("y", "n"):
            break
        print("\nInvalid Choice\n")
    if choice == "y":
        site_info = sql.format_info(site_info)
        sql.add_to_database(domain, site_info)
            
