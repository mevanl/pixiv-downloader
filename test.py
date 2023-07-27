import json
import os 
import config
from pixivpy3 import * 
from config import config
from modules.Artwork import Artwork
from modules.download_ugoira import download_ugoira

api = AppPixivAPI()
REFRESH_TOKEN = config('REFRESH_TOKEN')
api.auth(refresh_token=REFRESH_TOKEN)


# User has given us an illustration ID, we save it as dictionary (jsonDICT)
raw_illust_json = api.illust_detail(85162550) 

# Handle if illust doesnt exist here
if raw_illust_json.get('error'):
    print("ERROR: This illustration does not exist or it is not possible to view this content.")
else: # Remove else once in function, unneeded since return 

    artwork = Artwork(raw_illust_json['illust'])
    if artwork.type == 'ugoira':
        ugoiraDict = api.ugoira_metadata(artwork.id) #  HAS UGOIRA ZIP LINK TO ALL IMAGES, AND HAS FRAME TIMES
        artwork = Artwork(raw_illust_json['illust'], ugoiraDict['ugoira_metadata'])
        #ugoiraDict = json.dumps(ugoiraDict, indent=4)
        #print(ugoiraDict)
        for i in artwork.download_urls():
            api.download(i, name='archive.zip')  # THIS WORKS FOR DOWNLOADING ZIPPED VERSION OF UGORIA 
        download_ugoira(ugoiraDict['ugoira_metadata']['frames'])
            

    #for i in artwork.download_urls():
        #api.download(i)



#  Print into json, helps for getting keys
#illust_json = json.dumps(raw_illust_json, indent=4)
#print(illust_json)


