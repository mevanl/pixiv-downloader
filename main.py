from pixivpy3 import *
from modules.download_artwork import download_artwork
from config import config

def menu():
    while True:
        print("\n\n\tPIXIV SCRIPT\t\n")
        print("1. Download Artwork\n2. Download Novel\n3. Quit")

        choice = input("Choose an option by entering the number (i.e. enter '1'): ")
        match choice:
            case "1":
                art_id = input("Enter Artwork ID: ")
                download_artwork(api, art_id)
            case "2":
                print("Novel")
            case "3":
                quit()
                

if __name__ == "__main__":
    api = AppPixivAPI()
    REFRESH_TOKEN = config('REFRESH_TOKEN')
    api.auth(refresh_token=REFRESH_TOKEN)

    menu()
