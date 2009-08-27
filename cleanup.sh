# Cleans out system from traces of Fluke

echo Deleting Fluke and its libraries..
rm -rf ./dist/Fluke.app
sudo rm -rf /Applications/Fluke.app /Library/QuickTime/XiphQT.component /Library/QuickTime/FlacImport.component

echo Cleaning up the application associations..
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user

echo Relaunching Finder
killall Finder && open /System/Library/CoreServices/Finder.app
echo Ok. Done. Phew.

