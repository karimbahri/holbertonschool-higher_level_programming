#!/bin/bash
# json post
curl -X POST -s -H "Content-Type: application/json" -d "$1" @"$2"
