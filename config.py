import configparser
import pathlib

def config(key: str) -> str:    
    configPath = pathlib.Path(__file__).parent.absolute()
    configFile = configparser.ConfigParser()
    print(configPath)
    configFile.read(str(configPath)+"\config.ini")

    if key == 'REFRESH_TOKEN':
        return configFile['REFRESH_TOKEN']['Refresh_Token']



