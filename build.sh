echo "Building Fluke..."
rm -rf ./dist/Fluke.app
python setup.py py2app --plist ./resources/Info.plist --iconfile ./resources/Fluke.icns --prefer-ppc
