# Fluke uninstall script

clear
read -p "This will uninstall Fluke. Press any key to continue.."

echo -n Deleting Fluke and its libraries...
sudo rm -rf /Applications/Fluke.app /Library/QuickTime/XiphQT.component /Library/QuickTime/FlacImport.component
echo OK


echo -n Cleaning up application associations...
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user
echo OK

echo Ok. Done. Phew.

