import json
import config
from pixivpy3 import * 
from config import config

api = AppPixivAPI()
REFRESH_TOKEN = config('REFRESH_TOKEN')
api.auth(refresh_token=REFRESH_TOKEN)


# User has given us an illustration ID, we save it as dictionary (jsonDICT)
raw_illust_json = api.illust_detail(85162550) 

# POSSIBLE FEATURE: Type check to ensure its illust type ? Idk if api allows such tbh since some novels and illus have same ID  ???


# Handle if illust doesnt exist here
if raw_illust_json.get('error'):
    print("ERROR: This illustration does not exist or it is not possible to view this content.")
    #  return
else: # Remove else once in function, unneeded since return 
    illust = raw_illust_json['illust']

    # Check if multiple or single illstrations 
    if illust['page_count'] > 1:
        print("multi-page")
        #for i in range(0, illust['page_count']):
            #api.download(illust['meta_pages'][i]['image_urls']['original'])  # Downloads all illustrations
    else:
        print("singe-page")
        api.download(illust['meta_single_page']['original_image_url'])  # Downloads single illustration 



#  Print into json, helps for getting keys
illust_json = json.dumps(raw_illust_json, indent=4)
print(illust_json)


