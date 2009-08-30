#
#  main.py
#  Fluke
#
#  Created by Dmitry Kichenko on 24/08/09.
#  Copyright University of Toronto 2009. All rights reserved.
#

#import modules required by application
import objc
import AppKit
import Foundation

from PyObjCTools import AppHelper


# import modules containing classes required to start application and load MainMenu.nib
import FlukeAppDelegate, FlukeController

#f = Fluke.Fluke.alloc().init()
#f.openFileDialog()

# pass control to AppKit
AppHelper.runEventLoop()
