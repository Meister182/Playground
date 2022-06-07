#!/bin/bash
LVL_2_VAR="something from level 2"
export LVL_2_VAR

echo "LVL 2:" $LVL_2_VAR

function change_lvl1_var() {
	LVL_1_VAR="changed in level 2"
}
change_lvl1_var
