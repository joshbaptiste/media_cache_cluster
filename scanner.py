#!/usr/bin/env python3

import os

class Scanner:
    "Scans directories and generates dir entries"

    def __init__(self):
        REMOTE_DIR = config.REMOTE_DIR
        CACHE_DIR = config.CACHED_DIR
    
    def scanDirectory(self, path):
        with os.scandir(path) as files:
            for fn in files:
                if fn.is_file():
                    yield fn.name

    def createSymLinks(self, src, dst): 
        os.symlink(src, dst) 
        
    def removeSymLink(self, src, dst):
        pass 
        
    def updateSymLink(self): 
        pass
