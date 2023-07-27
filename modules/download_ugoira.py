from zipfile import ZipFile
import os
import shutil
from PIL import Image


def download_ugoira(ugoira_frames: dict) -> None:
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
    imageList[0].save('archive.gif', save_all=True, append_images=imageList[1:], optimize=False, duration=durationList, loop=0)

    #  delete the extracted zip and the zip itself, only left with gif
    shutil.rmtree('archive')
    os.remove('archive.zip')