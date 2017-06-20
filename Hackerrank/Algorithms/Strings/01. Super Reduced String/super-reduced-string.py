#!/bin/python3

import sys


def super_reduced_string(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # pair of adjacent letters found, remove
            # and decrement index for a`bb`a edge case
            s = s[:i] + s[i + 2:]
            i = i - 1 if i > 0 else 0
        else:
            # no pair increment index
            i += 1
    return s if len(s) > 0 else "Empty String"


def main():
    print(super_reduced_string(input().strip()))


if __name__ == '__main__':
    main()
