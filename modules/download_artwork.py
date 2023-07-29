from modules.artwork import Artwork
from modules.download_ugoira import download_ugoira
from settings import formatter
import os

 
def download_artwork(api, artwork_id: int) -> None:
    """
    parameters: 
    -artwork_id allows us to identify which image the user wishes to download
    """
    artwork_jsonDICT = api.illust_detail(artwork_id)

    #  If image does not exist, privated, etc. 
    if artwork_jsonDICT.get('error'):
        print('Error! This artwork does not exist or it is not possible to access this content.')
        return
    
    artwork = Artwork(artwork_jsonDICT['illust'], (api.ugoira_metadata(artwork_id)))

    #  Handles downloading ugoira 
    if artwork.type == 'ugoira':
        for i in artwork.download_urls():
            api.download(i, name='archive.zip')
        download_ugoira(api.ugoira_metadata(artwork_id)['ugoira_metadata']['frames'], art=artwork)
        return
    
    #  Handles downloading multiple or single illustrations/Manga on one post. 
    print('Download Starting...')
    page: int = 0
    for i in artwork.download_urls():
        print(f'Downloading {i}')
        if artwork.type == 'illust':
            api.download(i, 
                         path=formatter(path=os.environ.get("ILLUST_PATH"), art=artwork), 
                         name=formatter(filename=os.environ.get("ILLUST_FILENAME"), art=artwork, pagenum=page))
        else:
            api.download(i, 
                        path=formatter(path=os.environ.get("MANGA_PATH"), art=artwork),
                        name=formatter(filename=os.environ.get("MANGA_FILENAME"), art=artwork, pagenum=page))             
        page += 1
    print(f'Download finished.')
    return
 