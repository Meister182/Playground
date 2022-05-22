#!/bin/bash
function argument_parser(){
    while [ $# -gt 0 ]; do
        case "$1" in
            -h |--help) help;;
            -a |--arg) argument "$2";;
            -b |--bool) bool=true;;
        esac
        shift
    done
}

function help(){
    cat << HELPT_TEXT
    $0: argument parser experiment.
    -h/--help)      flag was used.
    -a/--arg)       passing an argument.
    -b/--bool)     flaging a boolean.
HELPT_TEXT
}

function argument(){
    echo "Received argument: " $1;
}

# --- main code ---
bool=false
argument_parser $@

if $bool; then
    echo "Bool is on."
else
    echo "Bool is off."
fi