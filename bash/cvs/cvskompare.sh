#!/bin/bash
cvs diff -Nu "$@" | kompare -
