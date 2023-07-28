from modules.novel import Novel

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

    print("Creating novel file...")
    novel_file = open(f'{novel.title}.txt', 'w', encoding='utf-8')
    print("Created novel file, adding text...")
    novel_file.write(novel.text)
    print("Download finished.")
    novel_file.close()
    return 