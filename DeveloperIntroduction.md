# Introduction #
The current version of Fluke is built on python and needs the following libraries to build:
  * [mutagen](http://code.google.com/p/mutagen/)
  * [appscript](http://appscript.sourceforge.net/py-appscript/index.html)

# Building #
Fluke builds best on a [MacPorts](http://www.macports.org/install.php) python install. You'll need these packages before you proceed:
```
python25, py25-py2app, py25-pyobjc2, py25-pyobjc2-cocoa
```
  1. Once you've got the right python, grab mutagen and appscript via easy\_install. Make sure you're using the correct easy\_install or you'll be installing under _/Library/Python_ which you don't want.
  1. If you haven't installed Fluke at all, copy Xiph.component and FLACImporter.component from the _installer_ folder to /Library/QuickTime
  1. Make sure you've got the latest py2app:
```
sudo easy_install -U py2app
```
  1. Build!
```
python setup.py py2app
```
  1. Use the optional **-A** flag at the end if you're just screwing around and not building for distribution.

# What it does #
The general program flow is like this:
  1. Clean up and process the input
  1. Add tracks via appscript
  1. Look up the missing metadata via mutagen (at the moment that would be the track numbers and total track count) and assign it via appscript
  1. Convert the tracks if the user specified it.