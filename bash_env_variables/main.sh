#!/bin/bash
#set -x

#TODO: Add comment description here
scripts_dir=$(realpath "$(dirname "$0")")

source "${scripts_dir}"/script_lvl_1.sh $scripts_dir

if [ -n "$(env | grep LVL_1_VAR)" ]; then
	echo $LVL_1_VAR
else
	echo "Did not found Level 1 variable.."
fi

# source "${scripts_dir}"/script_lvl_2.sh
if [ -n "$(env | grep LVL_2_VAR)" ]; then
	echo $LVL_2_VAR
else
	echo "Did not found Level 2 variable.."
fi
