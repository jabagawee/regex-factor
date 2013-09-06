#! /usr/bin/env python

import re
import sys

r = re.compile(r"^(aa+?)\1+$")

def factor(n):
    match = r.match("a" * n)
    if not match:
        return [n]
    f = len(match.groups()[0])
    return factor(f) + factor(n/f)

if __name__ == "__main__":
    print factor(int(sys.argv[1]))
