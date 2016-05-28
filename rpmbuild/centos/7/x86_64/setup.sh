#!/bin/sh


d=`dirname $0`

[ "$d" = "." ] && d=`pwd`

echo "%_topdir $d" > $HOME/.rpmmacros 

exit $?
