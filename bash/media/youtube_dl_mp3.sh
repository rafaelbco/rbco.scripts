#!/bin/bash
youtube-dl --extract-audio --audio-format=mp3 --audio-quality=320K "$@"
