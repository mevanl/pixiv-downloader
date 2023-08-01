from modules.novel import Novel
import os
import shutil
from settings import formatter

def download_novel(api, novel_id: int) -> None:
    """
    parameters:
    -novel_id: int, allows us to indentify novel user wishes to download
    """
    novel_jsonDict = api.novel_detail(novel_id)

    #  If novel does not exist, privated, etc. 
    if novel_jsonDict.get('error'):
        print("ERROR: This novel does not exist or it is not possible to view this content.")
        return 
    
    novel = Novel(novel_jsonDict['novel'], api.novel_text(novel_id)['novel_text'])
    novel_title = formatter(filename=(os.environ.get("NOVEL_FILENAME")), novel=novel)
    novel_location = formatter(path=os.environ.get("NOVEL_PATH"), novel=novel)

    print("Creating novel file...")
    novel_file = open(novel_title, 'w', encoding='utf-8')
    print("Created novel file, adding text...")
    novel_file.write(novel.text)
    print("Download finished.")
    novel_file.close()
    try:
        shutil.move(os.path.curdir + "\\" + novel_title, novel_location)
    except shutil.Error:
        pass # Basically if they want to download it to the current directory of this program, it will throw an error saying it is already here
    return 