#!/bin/bash

## Run like
# echo abc def ghi | main_recomended.sh - NOK
# main_recomended.sh <<< abc def ghi	- OK -> if not quoted, only receives abc
# main_recomended.sh < file.txt		- OK

# runs if stdin file exists and is not empty
if [[ -s /dev/stdin ]]; then
  echo "received from stdin: $(cat -)"
else
  echo "Did not receive any input from stdin.."
fi
