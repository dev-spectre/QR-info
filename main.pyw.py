import setup
import mysqlConfig
import gui
import os

if __name__ == "__main__":

    gui.write_json({})

    path = "./templates/img/temp"
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
        
    gui.app()
