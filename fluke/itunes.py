"""
Module for dealing with iTunes stuff.
"""

import sys, os

# Fluke specific modules
from appscript import *
from mutagen.flac import *

def add(f):
    """Add tracks to iTunes and assign proper track numbers."""

    metadata = FLAC(f) # metadata pulled from .flac 
    ASFilePath = getASPath(f) # AppleScript friendly path

    track = app(u'iTunes').add( ASFilePath, to=app.library_playlists[1])
    if metadata.has_key('tracknumber'):
        track.track_number.set( metadata['tracknumber'] )

    #print str(track.track_number.get()) + ' "' + track.name.get() + '" - OK '

def convert(f):
    """Convert imported tracks into Apple Lossless"""
    # to be continued

def getASPath(path):
    """Return AppleScript-friendly path"""
    return ASStartupDisk() + path.replace("/",":")
    
def ASStartupDisk():
    """Return current startup disk. No relation to asses."""
    return app(u'Finder').startup_disk.name.get()

def setFileTypeToOggs(fn):
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
