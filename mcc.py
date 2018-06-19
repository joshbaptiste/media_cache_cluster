import configparser
import psutil
import scanner



def parseConfig(configFile):
    """ Parses config file """
    options = []
    config = configparser.ConfigParser()
    config.read(configFile)
    if config.has_section('global'):
        sections = config.sections()
        log.info("Loading Sections:") 
        for section in sections:   
            value = config.get(section)
            log.info("Found Section: {} = {}".format(section, val))
            options.add(section, value)
    else:
        raise configparser.NoSectionError
     
    return options

def checkDiskUsage(path):
    pass
    

def scanLocalDir():
    """
        Scans Local directory which contain symlinks
    """
scandir = scanner.scanDirectory(config.LOCAL_DIR)
    


