#!/bin/bash
# displays size of webpage
curl -Is "$1" | grep "Content-Length:" | cut -d " " -f 2
