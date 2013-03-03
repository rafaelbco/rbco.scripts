#!/bin/bash
# USAGE: $0 HOST
# SSL handshake with HOST. HOST is like example.com:443
openssl s_client -connect $@

