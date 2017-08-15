# kaptain: GUI frontend for shell commands

A fork from http://kaptain.sourceforge.net/. Honours go to author Zsolt Térek.

> Kaptain is a universal graphical front-end for command line programs. It works on linux/UNIX platforms whereever Qt is available. Release 0.73 is using qmake and is compatible with Qt 4.
>
> Someone writes a simple script (so called grammar) which describes the possible arguments for a command line program and Kaptain brings up a friendly dialog to the user to set up the command line.

[Dokumentation of kaptain](http://kaptain.sourceforge.net/docs/kaptain.html)

This little repo:
 - stores a copy of the source code
 - provides some binary packages for installation
 - provides instructions for compilation
 - provides a dockerfile for kaptain in a docker image

# Packages
Currently, this repository provides 64-bit packages only.
## debian
kaptain is available in repositories for debian jessie: https://packages.debian.org/jessie/kaptain.
The provided packages can be installed on debian stretch, too. The package provided here is a copy from debian repository. [Download package kaptain for debian](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-2_amd64_debian.deb).
## Ubuntu, Mint and other forks of Ubuntu
kaptain is available in repositories of Ubuntu 14.04: http://packages.ubuntu.com/trusty/kaptain.
The provided packages can be installed on Ubuntu 16.04, too. The package provided here is a copy from Ubuntu repository. [Download package kaptain for Ubuntu](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-1_amd64_ubuntu.deb).

Most likely, the Ubuntu package of kaptain will work on other Ubuntu-based distributions like Linux Mint, too.
## fedora, CentOS, RHEL
This repository provides an rpm package for fedora. Compiled and packaged on fedora 25. [Download package kaptain for fedora](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-1.x86_64_fedora.rpm).

As directly related, the rpm package provided for fedora will most probably work on CentOS and RHEL, too. Though, this is not tested yet.
## openSUSE
This repository provides an rpm package for openSUSE. Compiled and packaged on openSUSE 42.3 LEAP. [Download package kaptain for openSUSE](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-1.x86_64_opensuse.rpm).

# Dockerfile and docker image
The [Dockerfile for kaptain](https://github.com/mviereck/kaptain/raw/master/Dockerfile) provided here is used for an automated built of [x11docker/kaptain](https://hub.docker.com/r/x11docker/kaptain/) on dockerhub. Example use: `x11docker --stdout --silent --hostdisplay --gpu --sharedir YOURKAPTNFILE -- x11docker/kaptain YOURKAPTNFILE`

# Compiling from source
The makefile of kaptain is configured to install everything in `/usr/local`. If you compile yourself, kaptain is installed as `/usr/local/bin/kaptain`. Manpage and documentation are in subfolders of `/usr/local`, too. `man kaptain` may not work then. Using the provided packages, all related files are stored at system locations they belong to. [Download: source code of kaptain](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.tgz).

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
# Porting to QT5
Unfortunately, kaptain is no longer maintained. As it is based on QT4 and not ported to QT5, it already disappears from official repositories. It is a quite useful tool and I am not aware of another one that is able to provide its features. Personally, I am using it as a frontend for [x11docker](https://github.com/mviereck/x11docker).

Is anyone out there who would like to port kaptain to QT5? :-)
