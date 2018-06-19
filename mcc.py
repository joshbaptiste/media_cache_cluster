import configparser
import psutil
import scanner



def parseConfig(configFile):
    config = configparser.ConfigParser()
    config.read(configFile)
    sections = config.sections()
    if sections.has_section('global'):
        pass
    else:
        raise configparser.NoSectionError
     

def checkDiskUsage():
    pass    
    

def scanLocalDir():
    """
        Scans Local directory which contain symlinks
    """
    scandir = scanner.scanDirectory(config.LOCAL_DIR)
    


