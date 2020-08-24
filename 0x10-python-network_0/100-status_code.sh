#!/bin/bash
# curl request link as arg
curl -o /dev/null -s -w "%{http_code}" "$1"
