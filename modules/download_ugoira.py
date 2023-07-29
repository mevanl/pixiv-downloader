from zipfile import ZipFile
import os
import shutil
from PIL import Image
from settings import formatter
from modules.artwork import Artwork


def download_ugoira(ugoira_frames: dict, art: Artwork) -> None:
    """
    Parameters:
    -ugoira_frames: dict, a dictionary of the frames (the images and duration) for the ugoira
    """
    
    imageList = []
    durationList = []

    #  Extract the zip we got from downloading from the api
    with ZipFile("archive.zip", 'r') as zip:
        zip.extractall(path=(os.path.curdir + "\\archive"))  # Will create a new folder to store the images in
    
    #  make the image files into image ojects and get each images duration it is active in the gif
    for i in range(0, ugoira_frames.__len__()):
        imageList.append(Image.open("archive\\"+ugoira_frames[i]['file']))
        durationList.append(ugoira_frames[i]['delay'])

    #  make the gif  
    ugoira_title = formatter(filename=os.environ.get('UGOIRA_FILENAME'), art=art)
    ugoira_location = formatter(path=os.environ.get("UGOIRA_PATH"), art=art)
    imageList[0].save(ugoira_title, save_all=True, append_images=imageList[1:], optimize=False, duration=durationList, loop=0)

    #  delete the extracted zip and the zip itself, only left with gif, then move to correct location 
    shutil.rmtree('archive')
    os.remove('archive.zip')
    shutil.move(os.path.curdir + "\\" + ugoira_title, ugoira_location)