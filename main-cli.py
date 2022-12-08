import setup
import mysqlConfig
from cli import *
    
if __name__ == "__main__":

    print()
    print("""
  QQQQQQQQ      RRRRRRRRRR 
 QQQQQQQQQQ     RRRRRRRRRRRR
QQQQ    QQQQ    RRRR     RRRR
QQQQ    QQQQ    RRRR     RRRR      IIIIIII NNN   NNN FFFFFFFF  OOOOOOO
QQQQ    QQQQ    RRRR     RRR         III   NNNN  NNN FFFFFFFF OOOOOOOOO
QQQQ    QQQQ    RRRRRRRRRRR          III   NNNNN NNN FFF      OOO   OOO
 QQQQQQQQQQQ    RRRRRRRRRRRRR        III   NNN NNNNN FFFFFF   OOO   OOO
  QQQQQQQQQQQQ  RRRR      RRRR       III   NNN  NNNN FFF      OOOOOOOOO
          QQQQQ RRRR       RRRR    IIIIIII NNN   NNN FFF       OOOOOOO 
""")

    while True:
        choice = ""
        while True:
            print()
            print("1. Scan QR")
            print("2. Exit", end = "\n\n")
            choice = input("Enter your choice (1/2): ") 
            if choice in ("1", "2"):
                break
            print()
            print("Invalid Choice")
        actions = { "1": scan_qr, "2": exit }
        action = actions.get(choice)
        qr_data, is_file_selected = action()
        if qr_data and is_url(qr_data):
            url = qr_data
            domain, site_info, from_database = get_site_info(url)
            print("URL:", url, end = "\n\n")
            print("Site Info", end = "\n\n")
            print(site_info)
            add_data_to_database(domain, site_info, from_database)
        elif qr_data and not is_url(qr_data):
            print("QR Data", end = "\n\n")
            print(qr_data)
        elif not qr_data and is_file_selected:
            print("Unable to extract data from image", end = "\n\n")
