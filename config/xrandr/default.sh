#!/bin/sh

source ~/.defaults

if [ -z $XRANDR_SETTINGS && -f $XRANDR_SETTINGS]; then
    sh $XRANDR_SETTINGS
fi
