#!/usr/bin/env python3

"""shellenv.py: imported module what displays enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os

#
# the function shell_env is an analog of shell-command ENV(1)
# 
def print_all():
    print ( '*** Print all environment variables ***' )
# Actually, output the environment variables are accessible in python's script
    for item, value in os.environ.items():
       print('{}: {}'.format(item, value))   
 
