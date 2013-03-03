#!/bin/bash
# USAGE: $0 CERT_PEM
openssl x509 -noout -text -in $1
