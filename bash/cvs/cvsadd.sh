#!/bin/bash
find . -type d -print0 | grep -zv CVS | xargs -0 cvs add
find . -type f -print0 | grep -zv CVS | grep -zv "\(CVS\|.*~$\)" | xargs -0 cvs add
