"""
Main Fluke class. Accepts a string or a list of files upon initiation.
"""
__all__ = ['itunes']

import sys,os
import itunes

class FLAC(object):
    def __init__(self,files=None):
        self.files = [] # list of lists with paths and references

        if files:
            self.files = [[f] for f in self.processFiles(self.argsToList(files)) ]

    def itunesAdd(self):
        """Add processed tracks to iTunes"""
        self.setFileTypeToOggs(self.filesPath())
        tracks = itunes.add( self.filesPath() ) 

        if tracks:
            for i in range(len(self.files)):
                self.files[i].append(tracks[i])

        else:
            print "Couldn't add the file(s). Please restart iTunes or reinstall Fluke."
            return False
        itunes.fixMetadata(self.filesList())
    
    def itunesConvert(self):
        """Convert added files to iTunes"""
        originalEnc = itunes.getEncoder() # save user's encoder and switch to lossless
        itunes.setEncoder( itunes.getEncoder('lossless') )

        for f in self.files:
            itunes.convert(f, delete=True)

        itunes.setEncoder(originalEnc) # set the encoder back to w/e user had it set to

    def filesList(self,files=None):
        """Get and set list of files to process"""
        if files:
            self.__init__(files)
        return self.files

    def filesPath(self):
        """Return list of paths to files"""
        return [f[0] for f in self.files]

    def filesItunes(self):
        """Return list of references to added songs in iTunes library"""
        return [f[1] for f in self.files]

    def processFiles(self, files):
        """
        Recurse through dirs if any are given and filter out non-flacs
        """
        import types
        results = []

        for f in files:
            if type(f) <> types.UnicodeType: f = unicode(f, errors='replace')

            if os.path.isdir(f):
                flacs = [os.path.abspath(os.path.join(f,s)) \
                         for s in os.listdir(f) if os.path.splitext(s)[1] == '.flac']
                results.extend(flacs)
            else: 
                if os.path.isfile(f) and os.path.splitext(f)[1] == '.flac':
                    results.append(os.path.abspath(f))

        return results

    def argsToList(self,args):
        """Check if argument was a list or a string. Always return a list"""        
        import types

        if type(args) == types.StringType:
            return [args]
        else:
            return list(args)

    def setFileTypeToOggs(self,fn):
        """Set filetype to OggS to allow playback in iTunes"""
        from Carbon import File, Files

        for f in fn:
            fl, is_dir = File.FSPathMakeRef(f.encode('utf-8'))
            if is_dir:
                return False
            ci, _fn, fsspc, pfl = fl.FSGetCatalogInfo(Files.kFSCatInfoFinderInfo)

            finfo = fsspc.FSpGetFInfo()
            finfo.Type = 'OggS'

            fsspc.FSpSetFInfo(finfo)
        return True

    def __str__(self):
        return str(self.files)
    def __repr__(self):
        return str(self.files)
