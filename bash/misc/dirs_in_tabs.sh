#!/bin/bash
# Open subdirectories of the working directory as tabs in x-terminal-emulator.
ls -1 -d */ | sed "s@^@--tab --working-directory=${PWD}/@" | xargs mate-terminal
