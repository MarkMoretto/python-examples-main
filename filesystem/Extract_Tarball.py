"""
Topic: Unzip Tarball (.tar) files

Date created: 03/08/18
"""

import tarfile
import os
import time

def getPathInfo():
    main = input('Please enter basepath and name for tar.gz file: ')
    dest = input('Please enter path to desination folder: ')
    return main, dest


def extractTar(main, dest):
    if(main.endswith('tar.gz')):
       tar = tarfile.open(main, 'r:gz')
       tar.extractall(path=dest)
       tar.close()
    elif(main.endswith('tar')):
         tar = tarfile.open(main, 'r:')
         tar.extractall(path=dest)
         tar.close()

def main():
    try:
        fullPath, outDir = getPathInfo()
        extractTar(fullPath, outDir)
        print('Thank you for using this program!')
        time.sleep(1)
        print('Goodbye!')
        time.sleep(1)
    except KeyboardInterrupt:
        if input('Key pressed. Restart extraction?') in ['y','yes','YES','Y']:
            extractTar(fullPath, outDir)
        else:
            print('Goodbye!')
            time.sleep(1)


if __name__ == '__main__':
    main()
