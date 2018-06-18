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
The provided packages can be installed on debian stretch, too. The package provided here is a copy from debian repository. 
 - [Download package kaptain for debian](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-2_amd64_debian.deb).
## Ubuntu, Mint and other forks of Ubuntu
kaptain is available in repositories of Ubuntu 14.04: http://packages.ubuntu.com/trusty/kaptain.
The provided packages can be installed on Ubuntu 16.04 and 18.04, too. The package provided here is a copy from Ubuntu repository. 
 - [Download package kaptain for Ubuntu](https://github.com/mviereck/kaptain/raw/master/kaptain_0.73-1_amd64_ubuntu.deb).

Most likely, the Ubuntu package of kaptain will work on other Ubuntu-based distributions like Linux Mint, too.
## fedora
This repository provides an rpm package for fedora. Compiled and packaged on fedora 25 with rpmbuild specification [kaptain-0.73.spec](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.spec). Tested on fedora 28.
 - [Download package kaptain for fedora](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-2.x86_64_fedora.rpm).
## CentOS, RHEL
This repository provides an rpm package for CentOS. Compiled and packaged on CentOS 7 with rpmbuild specification [kaptain-0.73.spec](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.spec). 
 - [Download package kaptain for CentOS](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-2.x86_64_centos.rpm).

As directly related, the rpm package provided for CentOS will most probably work on RHEL, too. Though, this is not tested yet.
## openSUSE
This repository provides an rpm package for openSUSE. Compiled and packaged on openSUSE 42.3 LEAP with rpmbuild specification [kaptain-0.73.spec](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.spec). 
 - [Download package kaptain for openSUSE](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73-2.x86_64_opensuse.rpm).

# Dockerfile and docker image
The provided [Dockerfile for kaptain](https://github.com/mviereck/kaptain/raw/master/Dockerfile) is used for an automated built of [x11docker/kaptain](https://hub.docker.com/r/x11docker/kaptain/) on docker hub. Example use: `x11docker --stdout --silent --hostdisplay --gpu --sharedir YOURKAPTNFILE -- x11docker/kaptain YOURKAPTNFILE`

# Compiling from source
 - [Download source code of kaptain](https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.tgz).

## Arch Linux, Manjaro
```
pacman -S qt4 bison flex
qmake-qt4 kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## debian
```
apt-get install libqt4-dev bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## Ubuntu
```
apt-get install libqt4-dev g++ bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## fedora
```
dnf install qt-devel bison flex
qmake-qt4 kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## CentOS
```
yum install qt-devel bison flex
qmake-qt4 kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## openSUSE
```
zypper install libqt4-devel bison flex
export QT_SELECT=qt4
qmake kaptain.pro
make
make install
mv /usr/local/bin/kaptain /usr/bin
mv /usr/local/share/doc/kaptain /usr/share/doc
mv /usr/local/share/kaptain /usr/share/kaptain
mv /usr/local/share/man/man1/kaptain.1 /usr/share/man/man1
```
## removing self-compiled kaptain
```
rm /usr/bin/kaptain
rm -R /usr/share/doc/kaptain
rm -R /usr/share/kaptain
rm /usr/share/man/man1/kaptain.1
```
# Porting to QT5
Unfortunately, kaptain is no longer maintained. As it is based on QT4 and not ported to QT5, it already disappears from official repositories. It is a quite useful tool and I am not aware of another one that is able to provide its features. Personally, I am using it as a frontend for [x11docker](https://github.com/mviereck/x11docker).

Is anyone out there who would like to port kaptain to QT5? :-)
