#!/bin/bash
grep -B1 -r --include="*.tex" "([A-Z\-]\+)" .
