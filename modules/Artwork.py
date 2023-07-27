

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
        self.__pagecount = illust['page_count']

        #  User of Artwork 
        self.__userID = illust['user']['id']
        self.__username = illust['user']['name']


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
    def page_count(self) -> int:
        return self.__pagecount
    
    @property
    def userID(self) -> int:
        return self.__userID
    
    @property
    def username(self) -> str:
        return self.__username
    
    def download_urls(self) -> list:
        url_list: list = []     
        if self.type == 'ugoira':
            url_list.append(self.ugoira_metadata['zip_urls']['medium'])
            return url_list
        elif self.page_count > 1:
            for i in range(0, self.page_count):
                url_list.append(self.illust['meta_pages'][i]['image_urls']['original'])
            return url_list
        else:
            url_list.append(self.illust['meta_single_page']['original_image_url'])
            return url_list
        
    def __str__(self) -> str:
        return f'id: {self.id}\nType: {self.type}\ndownload_urls: {self.download_urls()}'