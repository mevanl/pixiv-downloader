from pixivpy3 import *
from modules.download_image import download_image
from config import config

def menu():
    while True:
        print("\n\n\tPIXIV SCRIPT\t\n")
        print("1. Download Illustration/Manga")

        choice = input("Choose an option by entering the number (i.e. enter '1'): ")
        match choice:
            case "1":
                ill_id = input("Enter illustration ID: ")
                download_image(api, ill_id)
                

if __name__ == "__main__":
    api = AppPixivAPI()
    REFRESH_TOKEN = config('REFRESH_TOKEN')
    api.auth(refresh_token=REFRESH_TOKEN)

    menu()
