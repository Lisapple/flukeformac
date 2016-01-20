**Fluke** is a small utility for Mac OS that lets you play FLAC files right within iTunes.

## Features ##
  * 16bit/44.1KHz playback
  * Multiple file and folder handling (the latter from command line only at the moment)
  * Track number and count support

## Known issues ##
  * **Mac OS X 10.7 Lion Support**: is incomplete at this time. To make Fluke run, go into your Applications, right-click on iTunes, head to Get Info, and check off "Open in 32-bit Mode".
  * **Only 16bit/44.1KHz** files play fine. Any other resolution affects the speed of playback which is a known Xiph.org issue.
  * **Embedded artwork** is not supported. However if you've got an iTunes Store account, select the songs you added, right-click and hit _Get Album Artwork_.
  * **iPod, iPhone, iPad, Airport Express, Apple TV** and other devices from Apple are **NOT** supported — Fluke uses a third-party library not available on those devices.
  * **CD burning** does not work for the same reason as the above.

## TODOs ##
  * Folder handling via GUI
  * Offer option to convert to Apple Lossless on the spot