"""
Module for dealing with iTunes stuff.
"""

import sys, os

# Fluke specific modules
from appscript import *
from mutagen.flac import *

itunesApp = app(u'iTunes')

def add(f):
    """Add tracks to iTunes and assign proper track numbers."""

    metadata = FLAC(f) # metadata pulled from .flac 
    ASFilePath = getASPath(f) # AppleScript friendly path
    track = itunesApp.add( ASFilePath, to=app.library_playlists[1])
    
    # TODO Try to tag after adding for a possible speed gain
    if track:
        if metadata.has_key('tracknumber'):
            track.track_number.set( metadata['tracknumber'] )
        return track
    else:
        return False

def convert(f, delete=False):
    """Convert imported tracks into Apple Lossless"""
    from os import remove

    path = f.location().path
    f.convert()

    if delete:
        f.delete()
        remove(path)
    
def getEncoder(type=None):
    if type == 'lossless':
        return itunesApp.encoders[u'Lossless Encoder'].get()
    else:
        return itunesApp.current_encoder.get()

def setEncoder(enc):
    itunesApp.current_encoder.set(enc)

def getASPath(path):
    """Return AppleScript-friendly path"""
    return ASStartupDisk() + path.replace("/",":")
    
def ASStartupDisk():
    """Return current startup disk. No relation to asses."""
    return app(u'Finder').startup_disk.name.get()

