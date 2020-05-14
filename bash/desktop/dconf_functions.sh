#!/bin/bash

# Convert from a path like "/some/thing/org.my.app.dconf" to -> "/org/my/app/"
function file_to_dconf_path () {
    echo "/$(basename $1 | tr '.' '/' | sed  's/dconf$//')"
}

export -f file_to_dconf_path
