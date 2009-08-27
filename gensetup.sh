# Generates the setup.py with all the settings

py2applet --make-setup FlukeController.py --plist Info.plist --iconfile Fluke.icns --resources ./resources/Fluke-Flac.icns 
echo ==============
echo IMPORTANT: Check setup.py to see if '--plist', '--iconfile' and '--resources' are listed as part of the DATA_FILES list and if so, remove them (only the Fluke-Flac.icns should be listed as a resource)
