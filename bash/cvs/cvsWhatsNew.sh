#!/bin/sh
###############################################################################
#                                                                             #
#                               cvsWhatsNew.sh                                #
#                                                                             #
###############################################################################
#                                                                             #
#  Description:   A script to summarize which, if any, files in the current   #
#                 CVS working directory ("sandbox") have actually changed.    #
#                                                                             #
#  Author:        Mark Zieg <mark.zieg@lmco.com>                              #
#                                                                             #
#  Date:          Aug 27, 2002                                                #
#                                                                             #
#  Notes:         For most files, this is nothing more than a formatted       #
#                 wrapper around "cvs -n update".  However, in PRISM-land,    #
#                 Makefiles are dynamically modified during builds.  This     #
#                 means that they _ALWAYS_ show up as "modified" according    #
#                 to CVS, even though they aren't -- not in any significant   #
#                 way.  Therefore, this script pays special attention to      #
#                 PRISM Makefiles and tries to determine whether any of       #
#                 them have actually changed in a way that the developer      #
#                 would care about.                                           #
#                                                                             #
###############################################################################

#
# generate 'cvs -n update' results
#
DATA="/tmp/cvsWhatsNew.$$.dat"
TMP="/tmp/cvsWhatsNew.$$.tmp"
cvs -n update > $DATA 2>&1

#
# report modified local files
#
grep '^[MAR] ' $DATA | grep -v '^\?' | grep -iv Doxygen/html | sort > $TMP
if [ -s $TMP ]
then
    echo "You have not yet committed the following modifications:"
    cat $TMP
    rm $TMP
    echo " "
fi

#
# report out-of-date local files
#
egrep '^[UCP] ' $DATA | grep -iv Doxygen/html | sort > $TMP
if [ -s $TMP ]
then
    echo "Your copies of the following are out of date:"
    cat $TMP
    rm $TMP
    echo " "
fi

#
# report new files that may be important
#
egrep '^\?' $DATA | grep -v 'Doxygen/html' | egrep -i '\.(h|c|cpp|pl|pm|sh|html|doc|ppt|xls|gif|png|jpg|txt)$' >> $TMP
egrep '^\?' $DATA | egrep -i 'Makefile|README' >> $TMP
if [ -s $TMP ]
then
    echo "You may have forgotten to add the following new files:"
    cat $TMP
    rm $TMP
    echo " "
fi

#
# report directories that are missing
#
grep -i 'new directory' $DATA | sort > $TMP
if [ -s $TMP ]
then
    echo "You are missing the following directories from the repository:"
    cat $TMP
    rm $TMP
    echo " "
fi

#
# Doxygen check
#
grep '^M data/Doxygen/html' $DATA 1>/dev/null 2>&1
if [ $? = 0 ]
then
    echo "Warning: if you do a commit from here, you will commit rendered HTML"
    echo " "
fi

#
# cleanup
#
rm -f $DATA $TMP
