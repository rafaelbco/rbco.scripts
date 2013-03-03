#!/bin/bash
svn st --no-ignore | grep "^I" | sed s/'I\s\+'//
