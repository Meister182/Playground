'''
GIVEN a flag as a limited amount of choices
AND a default value
WHEN the flag is called without a value

What happens? :/

Expectation is to use the default value.

================================================================================
= Tests
================================================================================
$ python3 main.py
args.choice = 3, args.other = None

$ python3 main.py --choice
args.choice = None, args.other = None

$ python3 main.py --choice 1          
args.choice = 1, args.other = None

$ python3 main.py --choice --other 2  
args.choice = None, args.other = 2

$ python3 main.py --choice 1 --other 2
args.choice = 1, args.other = 2

================================================================================
= Conclusion
================================================================================
* Without `nargs=?`
    * a value must always be passed to the flag or an error is thrown
* With `nargs=?`
    * if a value is not passed, the argument value will be None
* With a `default` value
     *The argument will have the default value when the flag is not provided

'''
import argparse

parser = argparse.ArgumentParser(prog='choices')
parser.add_argument(
        '--choice',
        choices=list(range(5)),
        default=3,
        type=int,
        nargs='?'
        )
parser.add_argument(
        '--other',
        type=int
        )
args = parser.parse_args()

print(f"{args.choice = }, {args.other = }")

