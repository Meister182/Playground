#!/bin/bash

## Experimenting with the syntax and white spaces when declaring functions.
# *personal favorite.
function my_print_1(){
    echo "this is function 1."
}

# White spaces seem irrelevant
function my_print_2 ()
{
    echo "this is function 2."
}

# More compact and it seems more compatible(Bourne/Korn/POSIX)
my_print_3(){
    echo "this is function 3."
}

my_print_1
my_print_2
my_print_3


## Experimenting with the declaration order.
# can a function call another one called after it?
# *Yes, as long as it is called after it is declred
function first_function(){
    echo "I'm first!"
    second_function
}

# Throws an error if called here: " line 25: second_function: command not found"
# first_function

function second_function(){
    echo "I'm second!"
}

first_function