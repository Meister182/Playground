#!/bin/bash
function argument_parser(){
    while [ $# -gt 0 ]; do
        case "$1" in
            -h |--help)
                help
            ;;
        esac
        shift
    done
}

function help(){
    cat << HELPT_TEXT
    $0: argument parser experiment.
    -h/--help)      flag was used."
HELPT_TEXT
}


# --- main code ---
argument_parser $@