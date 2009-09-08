"""
Fluke lets you play FLACs in iTunes. This the command line version of it.

USAGE

python flukeapp.py file1[ file2 file3...] [--convert]

file1,file2.. can be directories

--convert   automaticaly convert imported FLACs to Apple Lossless
"""

import sys,os
# py2app fix - make sure we're going to find those third part libs
resPath = sys.argv[0].split("/")
resPath.pop()
sys.path.insert( 0, os.path.join('/'.join([a for a in resPath]), 'lib', 'python2.5', 'lib-dynload') )

import fluke 

def cleanUpSysArgs(args):
    # Remove the script itself as an argument
    del(args[0])

    # Clean up the -psn argument Finder adds
    for i in range(len(args)):
        if args[i].startswith('-psn'): del(f)
        args[i] = args[i].decode('utf-8')
    
    return args

if __name__ == "__main__":
    sys.argv = cleanUpSysArgs(sys.argv)
    if len(sys.argv) == 0:
        print(__doc__)
    files = fluke.FLAC(sys.argv)
    files.itunesAdd()

    if "--convert" in sys.argv:
        files.itunesConvert()
