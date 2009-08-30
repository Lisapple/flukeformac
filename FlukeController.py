"""
Fluke controller for Xcode and py2app
"""
# PyObjC modules
import objc
from Foundation import *
from AppKit import *

from PyObjCTools import AppHelper

import sys,os

# py2app fix - make sure we're going to find those third part libs
#resPath = sys.argv[0].split("/")
#resPath.pop()
#sys.path.insert( 0, os.path.join('/'.join([a for a in resPath]), 'lib', 'python2.5', 'lib-dynload') )

import fluke 

class FlukeController(NSObject):

    mainWindow = objc.IBOutlet()
    
    checkboxDelete = objc.IBOutlet()
    
    def awakeFromNib(self):
        import flukeapp

        NSLog(str(self.mainWindow.canBecomeMainWindow()))

        sys.argv = flukeapp.cleanUpSysArgs(sys.argv)
        NSLog('System arguments: ' + str(sys.argv))
        
        # Open fileOpen dialog if no files were fed in
        #self.processFiles(sys.argv)
        
    @objc.IBAction
    def open_(self, sender):
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseDirectories_(True)
        panel.setAllowsMultipleSelection_(True)
        panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
             '~/', None, ('flac',), self.mainWindow,
             self, 'openPanelDidEnd:panel:returnCode:contextInfo:', 0)
             
    @objc.IBAction
    def toggleConversion_(self,sender):
        NSLog(str(sender.state()))
        if sender.state() == 1:
            self.checkboxDelete.setEnabled_(True)
        else:
            self.checkboxDelete.setState_(0)
            self.checkboxDelete.setEnabled_(False)

    @AppHelper.endSheetMethod
    def openPanelDidEnd_panel_returnCode_contextInfo_(self, panel, returnCode, contextInfo):
        if returnCode:
            print "Open: %s" % panel.filenames()
        else:
            print "Cancel"
            
    

        
if __name__ == "__main__":
    NSLog("hi!!!")
