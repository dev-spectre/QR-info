import qr
import sql
import json
import website
import eel
import os
import shutil
import tkinter
import tkinter.filedialog


info = None
url = None
file_name = None

@eel.expose
def select_file():
    global file_name
    win = tkinter.Tk()
    win.withdraw()
    win.attributes("-topmost", True)
    file_path = tkinter.filedialog.askopenfilename(parent = win)
    if file_path:
        file_name = os.path.basename(file_path)
        if os.path.splitext(file_name)[1] in [".png", ".jpg", ".jpeg"]:
            
            dest = f"./templates/img/temp/{file_name}"
            shutil.copy(file_path, dest)
            relative_path = f"./img/temp/{file_name}"
            eel.setImage(relative_path)

def write_json(data, file_name = "data"):
    with open(f"./templates/script/{file_name}.json", 'w') as file: 
        json.dump(data, file, indent = 4)
        file.close()

def read_json(key, file_name = "data"):
    with open(f"./templates/script/{file_name}.json", 'r') as file:
        json_object = json.load(file)
        file.close()
        print("read_json: json['editedInfo'] =", json_object[key])
        return json_object[key]

@eel.expose
def scan_qr():
    global url
    global info
    global file_name
    short_url = None
    file_path = f"./templates/img/temp/{file_name}"
    if os.path.isfile(file_path):
        data = qr.get_data(file_path)
        if data is None:
            data = "Unable to extract data from image"
        else:
            url = data
            short_url = website.get_short_url(url)

        if short_url is None:
            json_object = {
                "page" : "nolink.html",
                "data" : data
                }
            write_json(json_object)
            eel.redirect()
            return

        domain = website.extract_domain(short_url)
        result = sql.get_info(domain)

        if result is None:
            info = website.get_info_from_ai(short_url)
            json_object = {
                "page"   : "qrinfo.html",
                "url"    : url,
                "data"   : info,
                "infoFrom" : "AI"
                }
            write_json(json_object)
            eel.redirect()
            return

        info = result[0]
        json_object = {
            "page"     : "qrinfo.html",
            "url"      : url,
            "data"     : info,
            "infoFrom" : "Database",
            "addedBy"  : result[1]
            }
        write_json(json_object)
        eel.redirect()


@eel.expose
def add_info(data = info):
    domain = website.extract_domain(url)
    if data is None:
        return
    sql.add_to_database(domain, data)

def app():
    eel.init("templates")
    
    width = 900
    height = 600
    pos_x = 125
    pos_y = 50

    eel.start(
        "index.html", 
        port = 0,  
        size = (width, height), 
        position = (pos_x, pos_y),
        geometry = {
            "size": (width, height),
            "position": (pos_x, pos_y)
            }
        )
