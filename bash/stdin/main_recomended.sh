#!/bin/bash

## Run like
# echo abc def ghi | main_recomended.sh - OK
# main_recomended.sh <<< abc def ghi	- OK -> if not quoted, only receives abc
# main_recomended.sh < file.txt		- OK

# runs if stdin file descriptor is not open
if [[ ! -t 0 ]]; then
  echo "received from stdin: $(cat -)"
else
  echo "Did not receive any input from stdin.."
fi
