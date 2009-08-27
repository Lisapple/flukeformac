"""
Process input files
"""
__author__  = 'Dmitry Kichenko (dmitrykichenko@gmail.com)'
__license__ = 'Python'

import sys, os

class files (object):
    def __init__(self,files):
        if len(files) < 2:
            print "There is nothing for me to add to iTunes."
            return

        files = self.cleanUpArgs(files)
        self.processFiles(files)

    def processFiles(self, files):
        """
        Recurse through dirs if any are given and filter out flacs
        """
        for f in files:
            if os.path.isdir(f):
                flacs = [os.path.join(f,s) for s in os.listdir(f)
                        if os.path.splitext(s)[1] == '.flac']
                
                self.processFiles(flacs)
            else: 
                #self.iTunesAdd(f)
                print(f)
                continue

    def cleanUpArgs(self,args):
        """
        Remove reference to self and the '-psn' arg added by Finder from arguments
        """
        del(args[0])

        if args[0].startswith('-psn'):
            del(args[0])
        return args

