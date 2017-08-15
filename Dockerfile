# kaptain
#
# Kaptain is a universal graphical front-end for command line programs. 
# It works on linux/UNIX platforms whereever Qt is available. 
# Release 0.73 is using qmake and is compatible with Qt 4.
#
# Someone writes a simple script (so called grammar) which describes 
# the possible arguments for a command line program and Kaptain 
# brings up a friendly dialog to the user to set up the command line.
#
# https://github.com/mviereck/kaptain
#
# To use kaptain in this image, provide an X display and share your .kaptn file
# Example use with x11docker (https://github.com/mviereck/x11docker):
#   x11docker --stdout --stderr --sharedir YOURKAPTNFILE --hostdisplay --gpu -- x11docker/kaptain YOURKAPTNFILE

FROM debian:jessie
RUN apt-get  update
RUN apt-get install -y apt-utils

# Language/locale settings
ENV LANG=en_US.UTF-8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/default/locale
RUN apt-get install -y locales

RUN apt-get install -y --no-install-recommends kaptain

ENTRYPOINT /usr/bin/kaptain
