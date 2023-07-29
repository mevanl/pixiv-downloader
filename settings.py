import os
import dotenv
from modules.artwork import Artwork
from modules.novel import Novel


def defaults():

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    #  If no refresh token, input the user to enter it and set it in .env 
    if not dotenv.get_key(dotenv_file, "REFRESH_TOKEN"):
        print("No Refresh Token loaded. Please put refresh token into .env.")
        token: str = input("Refresh Token: ")
        os.environ["REFRESH_TOKEN"] = token
        dotenv.set_key(dotenv_file, "REFRESH_TOKEN", os.environ["REFRESH_TOKEN"])

    #  If Illust path and filename is not set, set to current directory and filenames to artwork's id and current pagenumber
    if not dotenv.get_key(dotenv_file, "ILLUST_PATH"):
        os.environ["ILLUST_PATH"] = os.path.curdir
        dotenv.set_key(dotenv_file, "ILLUST_PATH", os.environ["ILLUST_PATH"])

    if not dotenv.get_key(dotenv_file, "ILLUST_FILENAME"):
        os.environ["ILLUST_FILENAME"] = '{art_id}_{art_pagenum}'
        dotenv.set_key(dotenv_file, "ILLUST_FILENAME", os.environ["ILLUST_FILENAME"])

    #  If manga path and filename is not set, set to current directory and filenames to artwork's id and current pagenumber
    if not dotenv.get_key(dotenv_file, "MANGA_PATH"):
        os.environ["MANGA_PATH"] = os.path.curdir
        dotenv.set_key(dotenv_file, "MANGA_PATH", os.environ["MANGA_PATH"])

    if not dotenv.get_key(dotenv_file, "MANGA_FILENAME"):
        os.environ["MANGA_FILENAME"] = '{art_id}_{manga_seriesTitle}_{art_pagenum}'
        dotenv.set_key(dotenv_file, "MANGA_FILENAME", os.environ["MANGA_FILENAME"])

    #  If ugoira path and filename is not set, set to current directory and filenames to artwork's id
    if not dotenv.get_key(dotenv_file, "UGOIRA_PATH"):
        os.environ["UGOIRA_PATH"] = os.path.curdir
        dotenv.set_key(dotenv_file, "UGOIRA_PATH", os.environ["UGOIRA_PATH"])

    if not dotenv.get_key(dotenv_file, "UGOIRA_FILENAME"):
        os.environ["UGOIRA_FILENAME"] = '{art_id}'
        dotenv.set_key(dotenv_file, "UGOIRA_FILENAME", os.environ["UGOIRA_FILENAME"])

    #  If novel path and filename is not set, set to current directory and filenames to artwork's id
    if not dotenv.get_key(dotenv_file, "NOVEL_PATH"):
        os.environ["NOVEL_PATH"] = os.path.curdir
        dotenv.set_key(dotenv_file, "NOVEL_PATH", os.environ["NOVEL_PATH"])

    if not dotenv.get_key(dotenv_file, "NOVEL_FILENAME"):
        os.environ["NOVEL_FILENAME"] = '{novel_seriesTitle}: {novel_title}'
        dotenv.set_key(dotenv_file, "NOVEL_FILENAME", os.environ["NOVEL_FILENAME"])
        

def formatter(path: str=None, filename: str=None, pagenum: int=None, art: Artwork=None, novel: Novel=None):
    #  Art dict used to format the path and file in .env for custom paths and filenames 
    if art != None:
        art_key = {
            "art_id": art.id,
            "art_type": art.type,
            "art_title": art.title,
            "manga_seriesTitle": None,
            "manga_seriesID": None,
            "art_pagecount": art.page_count,
            "art_series": art.series,
            "art_pagenum": pagenum,

            "author_id": art.userID,
            "author_name": art.username
        }
        #  If type is manga, set the manga specific tags, will throw error if artwork isnt manga unless done like this 
        if art.type == 'manga':
            art_key["manga_seriesID"] = art.seriesID
            art_key["manga_seriesTitle"] = art.seriesTitle

        #  If working with non-novel format the path or filename with the art key dict, since we would only call either for path or for filename, dont need to get both at once
        if path != None:
            path = path.format(**art_key)
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        else:
            filename = filename.format(**art_key)
            filename = filename + art.filetype()
            return filename


    #  If working with novel format the path or filename with the novel key dict, since we would only call either for path or for filename, dont need to get both at once  
    if novel != None:
        #  Novel dict used to format the path and file in .env for custom paths and filenames 
        novel_key = {
            "novel_id": novel.id,
            "novel_title": novel.title,
            "novel_seriesID": novel.seriesID,
            "novel_seriesTitle": novel.seriesTitle,
            "novel_pagecount": novel.page_count,
            "nove_date": novel.date,

            "author_id": novel.userID,
            "author_name": novel.username
        }

        if path != None:
            path = path.format(**novel_key)
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        else:
            filename = filename.format(**novel_key)
            filename = filename
            return filename



def illustration_filename():
    filename: str = input("Enter new filename: ")
    os.environ["ILLUST_FILENAME"] = filename
    dotenv.set_key(dotenv.find_dotenv(), "ILLUST_FILENAME", os.environ["ILLUST_FILENAME"])

def illustration_path():
    path: str = input("Enter new path: ")
    os.environ["ILLUST_PATH"] = path
    dotenv.set_key(dotenv.find_dotenv(), "ILLUST_PATH", os.environ["ILLUST_PATH"])
    

def illustration_menu():
    while True:
        
        print("\n\n1. Path\n2. Filename\n3. Back")
        menu_choice = input("Choose an option by entering the number (i.e. enter '1'): ")

        match menu_choice:
            case "1":
                illustration_path()
            case "2":
                illustration_filename()
            case "3":
                break
            case  _: 
                print("Invalid Input. Please Select either: 1, 2, or 3.")

def manga_filename():
    filename: str = input("Enter new filename: ")
    os.environ["MANGA_FILENAME"] = filename
    dotenv.set_key(dotenv.find_dotenv(), "MANGA_FILENAME", os.environ["MANGA_FILENAME"])

def manga_path():
    path: str = input("Enter new path: ")
    os.environ["MANGA_PATH"] = path
    dotenv.set_key(dotenv.find_dotenv(), "MANGA_PATH", os.environ["MANGA_PATH"])
    

def manga_menu():
    while True:
        
        print("\n\n1. Path\n2. Filename\n3. Back")
        menu_choice = input("Choose an option by entering the number (i.e. enter '1'): ")

        match menu_choice:
            case "1":
                manga_path()
            case "2":
                manga_filename()
            case "3":
                break
            case  _: 
                print("Invalid Input. Please Select either: 1, 2, or 3.")

def ugoira_filename():
    filename: str = input("Enter new filename: ")
    os.environ["UGOIRA_FILENAME"] = filename
    dotenv.set_key(dotenv.find_dotenv(), "UGOIRA_FILENAME", os.environ["UGOIRA_FILENAME"])

def ugoira_path():
    path: str = input("Enter new path: ")
    os.environ["UGOIRA_PATH"] = path
    dotenv.set_key(dotenv.find_dotenv(), "UGOIRA_PATH", os.environ["UGOIRA_PATH"])
    

def ugoira_menu():
    while True:
        
        print("\n\n1. Path\n2. Filename\n3. Back")
        menu_choice = input("Choose an option by entering the number (i.e. enter '1'): ")

        match menu_choice:
            case "1":
                ugoira_path()
            case "2":
                ugoira_filename()
            case "3":
                break
            case  _: 
                print("Invalid Input. Please Select either: 1, 2, or 3.")

def novel_filename():
    filename: str = input("Enter new filename: ")
    os.environ["NOVEL_FILENAME"] = filename
    dotenv.set_key(dotenv.find_dotenv(), "NOVEL_FILENAME", os.environ["NOVEL_FILENAME"])

def novel_path():
    path: str = input("Enter new path: ")
    os.environ["NOVEL_PATH"] = path
    dotenv.set_key(dotenv.find_dotenv(), "NOVEL_PATH", os.environ["NOVEL_PATH"])
    

def novel_menu():
    while True:
        
        print("\n\n1. Path\n2. Filename\n3. Back")
        menu_choice = input("Choose an option by entering the number (i.e. enter '1'): ")

        match menu_choice:
            case "1":
                novel_path()
            case "2":
                novel_filename()
            case "3":
                break
            case  _: 
                print("Invalid Input. Please Select either: 1, 2, or 3.")

def settings_menu():
    while True:

        print("\n\n\tSETTINGS")
        print("1. Illustration Settings")
        print("2. Manga Settings")
        print("3. Ugoira Settings")
        print("4. Novel Settings")
        print("5. Back to menu.")
        menu_choice = input("Choose an option by entering the number (i.e. enter '1'): ")

        match menu_choice:
            case "1":
                illustration_menu()
            case "2":
                manga_menu()
            case "3":
                ugoira_menu()
            case "4":
                novel_menu()
            case "5":
                break
            case  _:
                print("Invalid Input. Please Select either: 1, 2, 3, 4, or 5.")

                

