#!/usr/bin/env python
import sys
from gpm.cli import run

def main():
    args = sys.argv[1:]
    run(args)

if __name__ == "__main__":
    main()