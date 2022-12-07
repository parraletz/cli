#!/usr/bin/python3

import argparse
import sys
import json


args = sys.argv[1:]
list = []


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value


parser = argparse.ArgumentParser()
parser.add_argument('a', nargs='*')
parser.add_argument('-x',action='store_true')
parser.add_argument('-y',action='store_true')
parser.add_argument('-k', '--kwargs', nargs='*', action=ParseKwargs)

value = parser.parse_args()
print(f"{value.a}")
print(f"el valor de y: {value.y}")
print(f"el valor de x: {value.x}")
print(value.kwargs)