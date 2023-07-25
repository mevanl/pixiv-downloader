from pixivpy3 import *

 
def download_artwork(api, artwork_id: int) -> None:
    """
    parameters: 
    -artwork_id allows us to identify which image the user wishs to download
    """
    artwork_jsonDICT = api.illust_detail(artwork_id)

    #  If image does not exist, privated, etc. 
    if artwork_jsonDICT.get('error'):
        print('Error! This illustration does not exist or it is not possible to access this content.')
        return
    
    artwork = artwork_jsonDICT['illust']

    #  Handles downloading multiple or single illustrations on one post. 
    if artwork['page_count'] > 1:
        print('Download Starting...')
        for i in range(0, artwork['page_count']):
            print(f'Downloading page {i}')
            api.download(artwork['meta_pages'][i]['image_urls']['original'])
        print(f'Download finished. {i+1} illustrations downloaded.')
        return
    else:
        print('Download Starting.')
        api.download(artwork['meta_single_page']['original_image_url'])
        print('Download Finished.')
        return