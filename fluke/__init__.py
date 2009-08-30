"""
Main Fluke class. Accepts a string or a list of files upon initiation.
"""
__all__ = ['itunes']

import sys,os
import itunes

class FLAC(object):
    def __init__(self,files=None):
        self.fileList = [] # list of paths to files
        self.fileListItunes = [] # references to tracks within iTunes

        if files:
            files = self.checkArgs(files)
            self.fileList = self.processFiles(files)

    def itunesAdd(self):
        """Add processed tracks to iTunes"""
        for f in self.fileList:
            self.setFileTypeToOggs(f)
            i = itunes.add(f) 

            if i:
                self.fileListItunes.append(i)
            else:
                print "Couldn't add the file(s). Please restart iTunes or reinstall Fluke."
                return False
    
    def itunesConvert(self):
        """Convert added files to iTunes"""
        originalEnc = itunes.getEncoder() # save user's encoder and switch to lossless
        itunes.setEncoder( itunes.getEncoder('lossless') )

        for f in self.fileListItunes:
            itunes.convert(f, delete=True)

        itunes.setEncoder(originalEnc) # set the encoder back to w/e user had it set to

    def files(self,files=None):
        """Get and set list of files to process"""
        if files:
            self.__init__(files)
        return self.fileList

    def processFiles(self, files):
        """
        Recurse through dirs if any are given and filter out non-flacs
        """
        results = []
        for f in files: 
            if os.path.isdir(f):
                flacs = [os.path.join(f,s) for s in os.listdir(f)
                        if os.path.splitext(s)[1] == '.flac']
                
                results.extend(flacs)
            else: 
                if os.path.isfile(f):
                    results.append(f)

        return results

    def checkArgs(self,args):
        """Check if argument was a list or a string. Always return a list"""
        
        import types

        if type(args) == types.StringType:
            return [args]
        else:
            return list(args)

    def setFileTypeToOggs(self,fn):
        """Set filetype to OggS to allow playback in iTunes"""
        from Carbon import File, Files

        fl, is_dir = File.FSPathMakeRef(fn)
        if is_dir:
            return False
        ci, _fn, fsspc, pfl = fl.FSGetCatalogInfo(Files.kFSCatInfoFinderInfo)

        finfo = fsspc.FSpGetFInfo()
        finfo.Type = 'OggS'

        fsspc.FSpSetFInfo(finfo)
        return True

    def __str__(self):
        return str(self.fileList)
