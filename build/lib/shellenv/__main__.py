#!/usr/bin/env python3

""" shellenv-run.py: tests Python's module python-shellenv to display enviroment info"""

import os
import sys

"""
   The module python-shellenv runs command next as
 
      $ python3 -m 

   Or executes wrapper script in command line by
      
      $ py-shellenv

   And how it was written in setup.py  
"""
def main(argv=None)->None:
    from shellenv import functionality_check 
    sys.exit(functionality_check())

if __name__ == '__main__':
   main() 
