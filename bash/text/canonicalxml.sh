#!/bin/bash
# USAGE: $0 FILE
# Format XML into canonical form and print to STDOUT.
# See: https://en.wikipedia.org/wiki/Canonical_XML
xmllint --c14n $@
