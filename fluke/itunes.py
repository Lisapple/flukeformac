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
        try:
            track.track_number.set( metadata['tracknumber'] )
        except AttributeError:
            return False

def convert(f):
    """Convert imported tracks into Apple Lossless"""
    # to be continued

def getASPath(path):
    """Return AppleScript-friendly path"""
    return ASStartupDisk() + path.replace("/",":")
    
def ASStartupDisk():
    """Return current startup disk. No relation to asses."""
    return app(u'Finder').startup_disk.name.get()

