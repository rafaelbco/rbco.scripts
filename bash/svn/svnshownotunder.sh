#!/bin/bash
svn st | grep "^?" | sed s/'?\s\+'//
