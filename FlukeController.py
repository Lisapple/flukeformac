"""
Fluke controller
"""
# PyObjC modules
from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

from PyObjCTools import AppHelper

import sys,os

import fluke, flukeapp

class FlukeController(NSObject):

    mainWindow = IBOutlet()
    myAlertView = IBOutlet()
    fileCount = IBOutlet()
    expandedFiles = IBOutlet()
    buttonGo = IBOutlet()
    checkboxDelete = IBOutlet()
    progressIndicator = IBOutlet()
    
    arrayController = IBOutlet()
    
    files = []
    filenames = []
    
    def awakeFromNib(self):
        sys.argv = flukeapp.cleanUpSysArgs(sys.argv)
        NSLog('System arguments: ' + str(sys.argv))
        
        self.windowHeight_(self,130)
        self.buttonGo.setKeyEquivalent_(u'\r') # assign GO to return key
        
        # Open fileOpen dialog if no files were fed in
        #self.processFiles(sys.argv)
        self.open_(self)        
        
    @IBAction
    def open_(self, sender):
        """Open dialogue for when Fluke was opened on its own"""
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseDirectories_(True)
        panel.setAllowsMultipleSelection_(True)
        result = panel.runModalForTypes_(('flac',))
        
        if result == NSOKButton:
            self.fillList_(self, panel.filenames())
        else:
            NSApp.terminate_(self)
    
    @IBAction
    def addFiles_(self,sender):
        self.toggleProgressBar_(self)
        self.files.itunesAdd()
        self.toggleProgressBar_(self)
    
        
    def fillList_(self,sender,files):
        """Fill GUI out with filenames. Takes list of files."""
        self.mainWindow.makeKeyAndOrderFront_(self)
        self.files = fluke.FLAC(files)
                    
        self.filenames = [ NSDictionary.dictionaryWithDictionary_(
            {
                'filename' : os.path.splitext( os.path.split(f)[1] )[0],
                'filepath' : f
            }) for f in self.files.filesPaths() ]
        
        self.arrayController.rearrangeObjects() # refresh the table with new values
        
        self.setTextFileCount_(self,len(self.files))
    # GUI methods
    
    @IBAction
    def toggleFileList_(self,sender):
        """Set the height of the file list NSTableView"""
        fileListHeight = 210
        
        if sender.state() == 1:
            self.expandedFiles.setHidden_(False)
            self.expandedFilesHeight_(self,fileListHeight)
            self.windowHeight_(self,350)

        else:
            self.expandedFiles.setHidden_(True)
            self.expandedFilesHeight_(self,fileListHeight)
            self.windowHeight_(self,130)
    
    @IBAction 
    def toggleProgressBar_(self,sender):
        """Turn the spinning wheel on and off"""
        if self.progressIndicator.isHidden():
            self.progressIndicator.setHidden_(NO)
            self.progressIndicator.startAnimation_(self)
        else:
            self.progressIndicator.setHidden_(YES)
            self.progressIndicator.stopAnimation_(self)

    @IBAction
    def toggleButtonGo_(self,sender):
        """Disable the GO button when adding"""
        pass
        
    @IBAction
    def toggleConvertToLossless_(self,sender):
        """Toggle the Delete option when selecting Conver to lossless"""
        if sender.state() == 1:
            self.checkboxDelete.setEnabled_(True)
        else:
            self.checkboxDelete.setState_(0)
            self.checkboxDelete.setEnabled_(False)
        
    
    def setTextFileCount_(self,sender,count):
        """Set how many files are being converted"""
        self.fileCount.setStringValue_('Adding ' + str(count) + ' files')
    
    def expandedFilesHeight_(self,sender,height):
        """Adjust the height of the file list"""
        origin = self.expandedFiles.frame().origin
        size = self.expandedFiles.frame().size
        NSLog(str(self.mainWindow.frame()))
        self.expandedFiles.setFrame_(NSMakeRect(origin.x,origin.y-(height-size.height),508,height))
        
    def windowHeight_(self,sender,height):
        """Animate the window height as we toggle with expandedFilesHeight()"""
        origin = self.mainWindow.frame().origin
        size = self.mainWindow.frame().size
        self.mainWindow.setFrame_display_animate_(NSMakeRect(origin.x, \
            origin.y-((height-size.height)/2), size.width, height), YES, YES)
            
    def filenamesToDictionary_(sender,filename,filepath):
        result = {}
        result['filename'] = filename
        result['filepath'] = filepath
        
        return result
        
if __name__ == "__main__":
    NSLog("hi!!!")
