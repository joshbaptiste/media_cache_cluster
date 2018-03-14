#!/usr/bin/python3

import os

class Scanner:
    # Scans directories and generates dir entries

    def __init__():
        REMOTE_DIR = config.REMOTE_DIR
        CACHE_DIR = config.CACHED_DIR
    
    def scanner(self, path):
        with os.scandir(path) as files:
            for fn in files:
                if not fn.name.startswith('.') and fn.is_file():
                    print(fn.name)

    def createSymLinks(self):
        pass