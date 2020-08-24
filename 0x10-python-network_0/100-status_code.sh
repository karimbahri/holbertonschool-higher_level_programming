#!/bin/bash
# curl request link as arg
curl -sw "%{http_code}" "$1"
