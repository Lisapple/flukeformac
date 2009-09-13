"""
All exceptions pooled together for easy importing later
"""

class FlukeException(Exception): pass
class ItunesReferenceError(FlukeException): pass
class ItunesFormatError(FlukeException): pass
class ItunesNotInitialized(FlukeException): pass

class GUIFormatError(FlukeException): pass
class GUIItunesRestart(FlukeException): pass
