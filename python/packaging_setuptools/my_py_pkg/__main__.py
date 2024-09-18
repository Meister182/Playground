#! /usr/bin/env python3
"""
My custom setuptools python package
"""
import argparse

from my_py_pkg.mods.foo import print_foo

def arg_parser(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--foo",
        action="store_true",
        help="Print foo message."
    )

    return parser.parse_args(argv)


def main(argv=None):
    args = arg_parser(argv)

    print("Running my setuptools python package!")

    if args.foo:
        print_foo()

if __name__ == "__main__":
    main()
