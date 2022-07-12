#!/bin/bash

## Run like
# echo abc def ghi | main_recomended.sh - OK
# main_recomended.sh <<< abc def ghi	- NOK
# main_recomended.sh < file.txt		- NOK

# runs if stdin file is a pipe
if [[ -p /dev/stdin ]]; then
  echo "received from stdin: $(cat -)"
else
  echo "Did not receive any input from stdin.."
fi
