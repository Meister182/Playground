#!/bin/bash

# Experimenting with the syntax and white spaces
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