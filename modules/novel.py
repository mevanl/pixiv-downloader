

class Novel():
    def __init__(self, novel: dict, text: str) -> None:
        """
        parameters:
        -novel: dict, is dict version of an novel's metadata send with tag ['novel'] to class
        -text: str, the novel's text 
        """

        #  Novel
        self.__novel = novel
        self.__id = novel['id']
        self.__title = novel['title']
        self.__page_count = novel['page_count']
        self.__text_length = novel['text_length']
        self.__text = text
        self.__seriesID = novel['series']['id']
        self.__seriesTitle = novel['series']['title']

        #  Author 
        self.__userID = novel['user']['id']
        self.__username = novel['user']['name']

    
    @property
    def novel(self) -> dict:
        return self.__novel
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def page_count(self) -> int:
        return self.__page_count
    
    @property
    def text_length(self) -> int:
        return self.__text_length
    
    @property 
    def text(self) -> str:
        return self.__text

    @property
    def seriesID(self) -> int:
        return self.__seriesID
    
    @property
    def seriesTitle(self) -> str:
        return self.__seriesTitle
    
    @property
    def userID(self) -> int:
        return self.__userID
    
    @property
    def username(self) -> str:
        return self.__username
    