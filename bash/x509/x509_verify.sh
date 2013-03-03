#!/bin/bash
# USAGE: $0 CA_PEM CERT_PEM
# Verify CERT_PEM against CA_PEM (concatenated trusted certificates).
openssl verify -CAfile $1 $2


