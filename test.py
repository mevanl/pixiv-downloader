import json
import os 
import config
from pixivpy3 import * 
from config import config
from modules.Artwork import Artwork

api = AppPixivAPI()
REFRESH_TOKEN = config('REFRESH_TOKEN')
api.auth(refresh_token=REFRESH_TOKEN)


# User has given us an illustration ID, we save it as dictionary (jsonDICT)
raw_illust_json = api.illust_detail(110210896) 

# Handle if illust doesnt exist here
if raw_illust_json.get('error'):
    print("ERROR: This illustration does not exist or it is not possible to view this content.")
else: # Remove else once in function, unneeded since return 

    artwork = Artwork(raw_illust_json['illust'])

    for i in artwork.download_urls():
        api.download(i)


#  Print into json, helps for getting keys
#illust_json = json.dumps(raw_illust_json, indent=4)
#print(illust_json)


