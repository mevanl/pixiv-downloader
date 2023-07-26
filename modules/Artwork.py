

class Artwork():
    def __init__(self, illust: dict) -> None:
        """
        parameters: 
        - illust: dict, is jsonDICT version of an artwork send with tag ['illust'] to class
        """

        #  Artwork  
        self.__illust = illust  
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
        if self.page_count > 1:
            for i in range(0, self.page_count):
                url_list.append(self.illust['meta_pages'][i]['image_urls']['original'])
            return url_list
        else:
            url_list.append(self.illust['meta_single_page']['original_image_url'])
            return url_list