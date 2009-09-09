#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module for dealing with iTunes stuff.
"""

import sys, os

# Fluke specific modules
from appscript import *
from mutagen.flac import FLAC, FLACNoHeaderError

itunesApp = app(u'iTunes')

class ItunesReferenceError(Exception): pass
class ItunesFormatError(Exception): pass

def add(files):
    filesASPaths = [getASPath(f) for f in files]
    tracks = itunesApp.add( filesASPaths, to=app.library_playlists[1])
    return tracks

def fixMetadata(files):
    print('FIXING METADATA: ' + str(files))
    for path,track in files:
        try:
            metadata = FLAC(path) # metadata pulled from .flac 
        except (FLACNoHeaderError):
            # Lack of proper FLAC header is not necessarily a bad FLAC
            metadata = {}
        if isSong(track):
            if metadata.has_key('tracknumber'): 
                setTrackNumber(track, metadata['tracknumber'][0])
        else:
            deleteTrack(track)
            raise ItunesFormatError(path + " is not a FLAC file.")

def setTrackNumber(track, tracknumber):
    if '/' in tracknumber: # if both the track # and count are given, split them
        tracknumber, trackcount = tracknumber.split('/')
        track.track_count.set(trackcount)
    track.track_number.set(tracknumber)

def convert(f, deleteFlac=False):
    """Convert imported tracks into Apple Lossless"""
    validateTrack(f)
    f.convert()
    if deleteFlac: deleteTrack(f)

def isSong(f):
    """Checks if track has a length i.e. wheter it's an actual song that can be played"""  
    validateTrack(f)
    return not hasattr(f.time.get(), 'name') and True or False

def validateTrack(f):
    """Checks if argument is a valid appscript reference & if the track is in the iTunes library"""
    from appscript.reference import Reference
    if isinstance(f, Reference) and hasattr(f, 'time'):
        return True
    else:
        raise ItunesReferenceError("Supplied argument is not a valid iTunes track.")        
        
def deleteTrack(f):
    """Delete a track from HDD and iTunes library"""
    path = f.location().path
    f.delete()
    os.remove(path)
    
def getEncoder(type=None):
    """Get currently set file encoder"""
    if type == 'lossless':
        return itunesApp.encoders[u'Lossless Encoder'].get()
    else:
        return itunesApp.current_encoder.get()

def setEncoder(enc):
    """Set an encoder. Takes reference to encoder, e.g. app('iTunes').encoders.get()[0]"""
    itunesApp.current_encoder.set(enc)

def getASPath(path):
    """Return AppleScript-friendly path"""
    path = path.replace('\ ', ' ') # AppleScript doesn't escape spaces
    p = path.split('/')

    # Put name of disk first if song not on startup disk
    if 'Volumes' in p:
        p = p[2:]
        return ':'.join([s for s in p])

    # Otherwise, prepend startup disk name to path
    return ASStartupDisk() + path.replace("/",":")
    
def ASStartupDisk():
    """Return current startup disk. No relation to asses."""
    return app(u'Finder').startup_disk.name.get()

