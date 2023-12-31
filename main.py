from pixivpy3 import *
from modules.download_artwork import download_artwork
from modules.download_novel import download_novel
import os
from settings import defaults, settings_menu

def menu():
    while True:
        print("\n\n\tPIXIV SCRIPT\t\n")
        print("1. Download Artwork\n2. Download Novel\n3. Settings\n4. Quit")

        choice = input("Choose an option by entering the number (i.e. enter '1'): ")
        match choice:
            case "1":
                art_id = input("Enter Artwork ID: ")
                download_artwork(api, art_id)
            case "2":
                novel_id = input("Enter Novel ID: ")
                download_novel(api, novel_id)
            case "3":
                settings_menu()
            case "4":
                quit()
            case  _:
                print("Invalid Input. Please Select either: 1, 2, 3, or 4.")
                

if __name__ == "__main__":
    defaults()

    api = AppPixivAPI()
    REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
    api.auth(refresh_token=REFRESH_TOKEN)

    menu()
