# kaptain
GUI frontend for shell commands

A fork from http://kaptain.sourceforge.net/. Honours go to author Zsolt Térek.

Kaptain is a universal graphical front-end for command line programs. It works on linux/UNIX platforms whereever Qt is available. Release 0.73 is using qmake and is compatible with Qt 4.

Someone writes a simple script (so called grammar) which describes the possible arguments for a command line program and Kaptain brings up a friendly dialog to the user to set up the command line.

[Dokumentation of kaptain](http://kaptain.sourceforge.net/docs/kaptain.html)

This little repo stores a copy of the source code and provides instructions for compilation. Also, it provides some binary packages.

Unfortunately, kaptain is no longer maintained, and as it is based on QT4 and not ported to QT5, it already disappears from official repositories. It is a quite useful tool and I am not aware of another one that is able to provide its features. Personally, I am using it as a frontend for [x11docker](https://github.com/mviereck/x11docker).

Is anyone out there who would like to port kaptain to QT5? :-)
# Packages
Currently, this repository provides 64-bit packages only.
## debian
kaptain is available in repositories for debian jessie: https://packages.debian.org/jessie/kaptain.
The provided package works on debian stretch, too. The package provided above is a copy from debian repository. [Download: package kaptain for debian](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-2_amd64_debian.deb).
## Ubuntu
kaptain is available in repositories of Ubuntu 14.04: http://packages.ubuntu.com/trusty/kaptain.
The provided package works on Ubuntu 16.04, too. The package above is a copy from Ubuntu repository. [Download: package kaptain for Ubuntu](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-1_amd64_ubuntu.deb).
#### Mint and other forks of Ubuntu
Most likely, the Ubuntu package of kaptain will work on other Ubuntu-based distributions, too.
## fedora
This repository provides an rpm package for fedora, see above. Compiled and packaged on fedora 25. [Download: package kaptain for fedora](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-1.x86_64_fedora.rpm).
#### CentOS, RHEL
As directly related, the rpm package provided for fedora will most probably work on CentOS and RHEL, too. Though, this is not tested yet.
## openSUSE
This repository provides an rpm package for openSUSE, see above. Compiled and packaged on openSUSE 42.3 LEAP. [Download: package kaptain for openSUSE](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-1.x86_64_opensuse.rpm).


# Compiling from source
The makefile of kaptain installs everything in `/usr/local`. If you compile yourself, kaptain is installed as `/usr/local/bin/kaptain`. Manpage and documentation are in `/usr/local`, too. `man kaptain` may not work then. Using the provided packages, all related files are stored at the system location they really belong to. [Download: source code of kaptain](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.tgz).

## debian
```
apt-get install libqt4-dev bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
```
## Ubuntu
```
apt-get install libqt4-dev g++ bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
```

## fedora
```
dnf install qt-devel bison flex
qmake-qt4 kaptain.pro
make
make install
```
## openSUSE
```
zypper install libqt4-devel bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
```
