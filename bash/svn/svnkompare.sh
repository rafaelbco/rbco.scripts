#!/bin/bash
svn diff $@ | kompare - &
