#!/bin/bash
# json post
curl -s -X POST -H "Content-Type: application/json" -d "$1" @"$2"
