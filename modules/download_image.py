from pixivpy3 import *

 
def download_image(api, illustration_id: int) -> None:
    """
    parameters: 
    -illustration_id allows us to identify which image the user wishs to download
    """
    illust_jsonDICT = api.illust_detail(illustration_id)

    #  If image does not exist, privated, etc. 
    if illust_jsonDICT.get('error'):
        print('Error! This illustration does not exist or it is not possible to access this content.')
        return
    
    illust = illust_jsonDICT['illust']

    #  Handles downloading multiple or single illustrations on one post. 
    if illust['page_count'] > 1:
        print('Download Starting...')
        for i in range(0, illust['page_count']):
            print(f'Downloading page {i}')
            api.download(illust['meta_pages'][i]['image_urls']['original'])
        print(f'Download finished. {i+1} illustrations downloaded.')
        return
    else:
        print('Download Starting.')
        api.download(illust['meta_single_page']['original_image_url'])
        print('Download Finished.')
        return