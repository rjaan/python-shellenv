#!/usr/bin/env python3

"""shellenv.py: imported module what displays enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os

#
# the function shell_env is an analog of C-function getenv(3)
# 
def getenv(keyenv):
    for key, value in os.environ.items():
       if keyenv == key : 
          return value
    return "" # return an empty text if nothings has been found   

#
# the function print_all is an analog of shell-command ENV(1)
# 
def print_all():
    print ( '*** Print all environment variables ***' )
# Actually, output the environment variables are accessible in python's script
    for key in os.environ:
       print('{}={}'.format(key, getenv(key)))   

      
