#!/bin/bash

if [ "$1" = "-full" ]; then
    # use the included metapackage to install basic stuff
    METADIR='jbertran-meta-setup'
    exec sudo sh -c "dpkg -i $METADIR/*.deb && apt-get -f install"
fi

which zsh && zsh deploy.sh
