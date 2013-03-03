#!/bin/sh

if [ "$* " != " " ]
then
    for foo in $*
    do    
        if [ -f $foo ]
        then
            echo "$foo:"
            # that is a literal tab after the ^
            cvs log $foo 2>/dev/null | grep "^	" | awk -F: '{print $1}' | awk '{print $1}' | sort -fu
            echo " "
        fi
    done
else
    echo "All tags found in under current directory:"
    echo " "
    # that is a literal tab after the ^
    cvs log 2>/dev/null | grep "^	" | awk -F: '{print $1}' | awk '{print $1}' | sort -fu
fi
