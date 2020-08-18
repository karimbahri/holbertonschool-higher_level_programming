#!/bin/bash
# post parametre
curl -LsX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
