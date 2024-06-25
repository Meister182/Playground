#!/bin/bash
set -x
# eval must be used


test_file="./test_file.txt"

# Remove a line with sed
cmd="sed \"/testing/d\""

cat "${test_file}" | eval "${cmd}"


