from pixivpy3 import *
from modules.Artwork import Artwork
from modules.download_ugoira import download_ugoira

 
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
    
    artwork = Artwork(artwork_jsonDICT['illust'], (api.ugoira_metadata(artwork_id))['ugoira_metadata'])

    #  Handles downloading ugoira 
    if artwork.type == 'ugoira':
        for i in artwork.download_urls():
            api.download(i, name='archive.zip')
        download_ugoira(api.ugoira_metadata(artwork_id)['ugoira_metadata']['frames'])
        return
    
    #  Handles downloading multiple or single illustrations/Manga on one post. 
    print('Download Starting...')
    for i in artwork.download_urls():
        print(f'Downloading {i}')
        api.download(i)
    print(f'Download finished.')
    return
 