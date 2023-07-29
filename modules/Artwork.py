import re

class Artwork():
    def __init__(self, illust: dict, ugoira_metadata=None) -> None:
        """
        parameters: 
        - illust: dict, is jsonDICT version of an artwork send with tag ['illust'] to class
        """

        #  Artwork  
        self.__illust = illust  
        self.__ugoira_metadata = ugoira_metadata
        self.__id = illust['id']
        self.__type = illust['type']
        self.__seriesID = None
        self.__seriesTitle = None
        self.__title = illust['title']
        self.__pagecount = illust['page_count']
        self.__series = None

        #  User of Artwork 
        self.__userID = illust['user']['id']
        self.__username = illust['user']['name']

    def remove_specialChar(self, text: str) -> str:
        text = re.sub("[\/:*?\"<>|]", "", text)
        return text
    
    @property
    def illust(self) -> dict:
        return self.__illust
    
    @property
    def ugoira_metadata(self) -> dict:
        return self.__ugoira_metadata
    @property 
    def id(self) -> int:
        return self.__id
    
    @property
    def type(self) -> str:
        return self.__type
    

    @property
    def seriesID(self) -> int:
        if self.type == 'manga':
            try:
                self.__seriesID = self.illust['series']['id']
                self.__seriesID = self.remove_specialChar(self.__seriesID)
                return self.__seriesID
            except Exception:
                self.__seriesID = "no series"
                return self.__seriesID
        
    @property
    def seriesTitle(self) -> str:
        if self.type == 'manga':
            try:
                self.__seriesTitle = self.illust['series']['title']
                self.__seriesTitle = self.remove_specialChar(self.__seriesTitle)
                return self.__seriesTitle
            except Exception:
                self.__seriesTitle = "No series"
                return self.__seriesTitle
    
    @property
    def title(self) -> str:
        self.__title = self.remove_specialChar(self.__title)
        return self.__title
    
    @property
    def page_count(self) -> int:
        return self.__pagecount
    
    @property
    def series(self) -> str:
        try:
            self.__series = self.illust['series']
            return self.__series
        except Exception:
            self.__series = "No series"
            return self.__series
    
    @property
    def userID(self) -> int:
        return self.__userID
    
    @property
    def username(self) -> str:
        self.__username = self.remove_specialChar(self.__username)
        return self.__username
    
    def filetype(self) -> str:
        if self.type == 'ugoira':
            extension = ".gif"
            return extension
        file_reference: str = self.illust['image_urls']['large']
        length = file_reference.__len__()
        extension = file_reference[length-4:]
        return extension
    
    def download_urls(self) -> list:
        url_list: list = []     
        if self.type == 'ugoira':
            url_list.append(self.ugoira_metadata['ugoira_metadata']['zip_urls']['medium'])
            return url_list
        elif self.page_count > 1:
            for i in range(0, self.page_count):
                url_list.append(self.illust['meta_pages'][i]['image_urls']['original'])
            return url_list
        else:
            url_list.append(self.illust['meta_single_page']['original_image_url'])
            return url_list
        