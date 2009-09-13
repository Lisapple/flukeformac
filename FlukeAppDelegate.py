#!/opt/local/bin/python
#
#  FlukeAppDelegate.py
#  Fluke
#
#  Created by Dmitry Kichenko on 24/08/09.
#  Copyright University of Toronto 2009. All rights reserved.
#

from Foundation import *
from AppKit import *
import sys
from FlukeController import *

class FlukeAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application finished launching.")
    
    def applicationShouldTerminateAfterLastWindowClosed_(self,sender):
        return True
