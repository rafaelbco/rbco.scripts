#!/bin/bash
hg diff $@ | kompare - &
