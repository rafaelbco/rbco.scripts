#!/bin/bash
# USAGE: sha1_fingerprint.sh CERT_PEM
openssl x509 -fingerprint -sha1 -noout -in $1
