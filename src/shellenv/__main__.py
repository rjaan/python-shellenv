#!/usr/bin/env python3

""" shellenv-run.py: tests Python's module python-shellenv to display enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import sys

"""
   This module runs command python3 -m or executes each individual function in 
   command line.
"""
  
if __name__ == '__main__':
       from shellenv import functionality_check 
       sys.exit(functionality_check())

