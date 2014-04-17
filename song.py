#!/usr/bin/env python

from __future__ import print_function
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage song.py text")
        sys.exit(1)

    for word in sys.argv[1:]:
        print(word)
        for c in word:
            char = ord(c)
            index = (char-20)%80
            index += 1
            print(ord(c), index)
        print()


if __name__ == '__main__':
    main()
