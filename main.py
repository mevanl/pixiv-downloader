from pixivpy3 import *
from modules.download_image import download_image
from config import config

def menu():
    while True:
        print("\n\n\tPIXIV SCRIPT\t\n")
        print("1. Download Illustration/Manga\n2. Download Ugoria\n3. Quit")

        choice = input("Choose an option by entering the number (i.e. enter '1'): ")
        match choice:
            case "1":
                ill_id = input("Enter illustration ID: ")
                download_image(api, ill_id)
                break
            case "2":
                print("UGORIA??")
                break
            case "3":
                quit()
                

if __name__ == "__main__":
    api = AppPixivAPI()
    REFRESH_TOKEN = config('REFRESH_TOKEN')
    api.auth(refresh_token=REFRESH_TOKEN)

    menu()
