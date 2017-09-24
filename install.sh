#!/bin/bash

if [ "$1" = "-full" ]; then
    # use the metapackage to install base dependencies
    METADIR='jbertran-meta-setup'

    make -C $METADIR package
    echo 'Root access required for metapackage installation'
    exec sudo sh -c  "dpkg -i $METADIR/$METADIR.deb; apt-get -f install"
    make -C clean
fi

zsh deploy.sh
