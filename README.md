<!-- Badges -->
[![](https://img.shields.io/github/v/release/ItaiShek/Wazzapp)](https://github.com/ItaiShek/Wazzapp/releases)
![](https://img.shields.io/github/downloads/ItaiShek/Wazzapp/total?color=red)
[![](https://img.shields.io/github/issues/ItaiShek/Wazzapp?color=yellow)](https://github.com/ItaiShek/Wazzapp/issues)
[![](https://img.shields.io/github/license/ItaiShek/Wazzapp?label=license&color=green)](https://github.com/ItaiShek/Wazzapp/blob/main/LICENSE)



* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Notes](#notes)
* [Todo](#todo)

# Description

When downloading an image from WhatsApp and opening it in Photoshop, you may encounter an error like this:

![Error](images/error.jpg "Photoshop error")

Photoshop may have trouble opening WhatsApp images directly, possibly due to how these images are saved. It seems they're often compressed and stored in a format that's best suited for viewing on mobile devices and sharing over messaging apps.

This software fixes it.


## Installation

### Windows:
[Installer](https://github.com/ItaiShek/Wazzapp/releases/latest/download/WazzappInstaller.msi) (The installer will add Wazzapp to the context menu)

[Portable](https://github.com/ItaiShek/Wazzapp/releases/latest/download/Win_Portable.zip)


## Usage
### Context menu
Right click inside/on a folder, or select multiple files.

![Context menu](images/Demo.gif "Windows context menu")


### Console
```
Wazzapp im1.jpg [im2.jpeg ...]
or
Wazzapp directory
```

## Notes
* The only difference between the executables is that one displays the messages via tkinter messagebox, while the other does so via the console.
* The JPEG files are overwritten by the software with the fixed versions. It creates a backup in the same directory as the original image, using the extension '.bak', and deletes it once the new file is successfully saved.
* The only affected files are JPEG/JPG images, other files/directories will be skipped.
* The identification of the JPEG format relies on the `imhdr` library, which can sometimes [overlook JPEG formats](https://github.com/python/cpython/issues/60716). I didn't experience any issues with it on WhatsApp images. If you're facing false negatives with WhatsApp images, feel free to open an issue, and I'll look into changing it.

## Todo
[ ] Create a macOS version.