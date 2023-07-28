import configparser
import pathlib
import os 

def Config(key: str) -> str:    
    configPath = pathlib.Path(__file__).parent.absolute()
    configFile = configparser.ConfigParser()
    print(configPath)
    configFile.read(str(configPath)+"\config.ini")

    unformatted_illust_path = configFile['ILLUSTRATION_DIRECTORY']['path']

    if key == 'REFRESH_TOKEN':
        return configFile['REFRESH_TOKEN']['Refresh_Token']
    
    if key == 'ILLUSTRATION_DIRECTORY':
        if not os.path.exists(configFile['ILLUSTRATION_DIRECTORY']['path']):
            os.makedirs(configFile['ILLUSTRATION_DIRECTORY']['path'])
        return configFile['ILLUSTRATION_DIRECTORY']['path']

