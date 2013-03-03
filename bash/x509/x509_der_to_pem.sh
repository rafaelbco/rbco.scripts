#!/bin/bash
# USAGE: $0 CERT_DER
openssl x509 -inform DER -outform PEM -in $1
