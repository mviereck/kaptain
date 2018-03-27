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
#   x11docker --stdout --clipboard --stderr --sharedir YOURKAPTNFILE --hostdisplay --gpu -- x11docker/kaptain YOURKAPTNFILE

FROM debian:jessie-slim
ENV DEBIAN_FRONTEND noninteractive

ENV LANG en_US.UTF-8
RUN echo $LANG UTF-8 > /etc/locale.gen && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends kaptain && \
    apt-get install -y locales && update-locale --reset LANG=$LANG && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "[QT]\n\
style=Cleanlooks\n\
" > /etc/xdg/Trolltech.conf

ENTRYPOINT ["/usr/bin/kaptain"]
ENV DEBIAN_FRONTEND newt
