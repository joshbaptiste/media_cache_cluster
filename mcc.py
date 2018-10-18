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
    try:
        du = psutil.disk_usage(path)
        return du
    except OSError:
        log.error("Unable to check disk usage of: " + path)
        

def scanLocalDir(config):
    """
        Scans Local directory which contain symlinks
    """
    
    log.info("Scanning directory ")
    scandir = scanner.scanDirectory(config.LOCAL_DIR)
    


