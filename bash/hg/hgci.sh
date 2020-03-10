#!/bin/bash
MESSAGES="auto-checkout
HISTORY
Prepara release
Refactoring"

echo "$MESSAGES" | hg ci -m "$(fzf)"
