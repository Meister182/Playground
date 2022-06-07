#!/bin/bash
LVL_1_VAR="something from level 1"
export LVL_1_VAR

echo "LVL 1:" $LVL_1_VAR

source $1/script_lvl_2.sh
