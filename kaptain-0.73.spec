#
# spec file for package kaptain
#
# Copyright (c) 2017 Martin Viereck <fizbaum-gmx-de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments to https://github.com/mviereck/kaptain

Summary:        GUI frontend for shell commands
Name:           kaptain
Version:        0.73
Release:        2
Source:         https://github.com/mviereck/kaptain/raw/master/kaptain-0.73.tgz
URL:            https://github.com/mviereck/kaptain
License:        GPLv2
Group:          Development/Tools/GUI Builders
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} 
BuildRequires:  qt-devel     bison flex
%endif
%if 0%{?suse_version}
BuildRequires:  libqt4-devel bison flex  
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       %{name} = %{version}

%description
Kaptain is a universal graphical front-end for command line programs. 
It works on linux/UNIX platforms whereever Qt is available. 
Release 0.73 is using qmake and is compatible with Qt 4.

Someone writes a simple script (so called grammar) which describes 
the possible arguments for a command line program and Kaptain brings up 
a friendly dialog to the user to set up the command line.

%prep
%setup -q
%build
export INSTALL_ROOT=%{buildroot}
export QT_SELECT=qt4

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} 
qmake-qt4 kaptain.pro
%else
#openSUSE
qmake     kaptain.pro
%endif

make

%install
export INSTALL_ROOT=%{buildroot}
make install

## adjust makefile installation pathes, use macros instead
cd %{buildroot}
# /usr/bin/kaptain
mkdir ./%{_bindir}
mv ./usr/local/bin/kaptain ./%{_bindir}
# docs
mkdir -p ./%{_defaultdocdir}
mv ./usr/local/share/doc/kaptain ./%{_defaultdocdir}
# example grammars
mkdir -p ./%{_datarootdir}
mv ./usr/local/share/kaptain .%{_datarootdir}
# manpage
mkdir -p ./%{_mandir}/man1
mv ./usr/local/share/man/man1/kaptain.1 ./%{_mandir}/man1
# remove /usr/local
rm -r ./usr/local

%files
%defattr(-,root,root)
%{_bindir}/*
%doc %{_defaultdocdir}/*
%doc %{_mandir}/*
%doc %{_datarootdir}/*

