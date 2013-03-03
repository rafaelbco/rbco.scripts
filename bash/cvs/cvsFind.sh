#!/bin/sh

#
# init
#
FILE="$1"
PATTERN="$2"
TMP="/tmp/cvsFind.$$.tmp"

#
# validate args
#
if [ "$FILE " = " " -o "$PATTERN" = " " ]
then
    echo "usage: cvsFind.sh <file> <search-regexp>"
    exit 1
fi
if [ ! -e $FILE ]
then
    echo "not found: $FILE"
    exit 1
fi
if [ ! -e CVS ]
then
    echo "not found: CVS"
    exit 1
fi

#
# get CVS metadata
#
REPO=`cat CVS/Repository`

#
# get revision list for this file
#
REVS=`cvs log $FILE | grep ^revision | awk '{print $2}'`

#
# find matching revisions
#
LAST_LEN=0
for REV in $REVS
do
    WIDTH=20
    LEN=`expr length $REV`
    if [ $LEN != $LAST_LEN ]
    then
        COUNT=`expr 20 - $LEN`
        DOTS=""
        while [ $COUNT != 0 ]
        do
            DOTS=".$DOTS"
            COUNT=`expr $COUNT - 1`
        done
    fi

    cvs -q checkout -p -r $REV $REPO/$FILE 2>/dev/null | egrep -n "$PATTERN" > $TMP
    if [ $? = 0 ]
    then
        cat $TMP | while read LINE 
        do
            echo -n "revision ${REV}${DOTS}MATCHED: "
            echo $LINE
        done
    else
        echo "revision ${REV}${DOTS}no"
    fi
    rm $TMP

    LAST_LEN=$LEN
done
    
