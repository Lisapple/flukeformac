"""
Fluke controller for Xcode and py2app
"""

import sys,os
# py2app fix - make sure we're going to find those third part libs
resPath = sys.argv[0].split("/")
resPath.pop()
sys.path.insert( 0, os.path.join('/'.join([a for a in resPath]), 'lib', 'python2.5', 'lib-dynload') )

# PyObjC modules
#import objc
#from Foundation import *
#from AppKit import *

import fluke 

if __name__ == "__main__":
    #[sys.argv.append(f) for f in files]
    
    # Remove the script itself as an argument
    del(sys.argv[0])

    # Clean up the -psn argument Finder adds
    for s in sys.argv:
        if s.startswith('-psn'): del(sys.argv[0])

    files = fluke.FLAC(sys.argv)
    files.itunesAdd()

    if "--convert" in sys.argv:
        files.itunesConvert()
