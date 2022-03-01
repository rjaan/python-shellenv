#!/usr/bin/env python3

"""myscripts.py: execute python code to display enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import shellenv

# We will run the module as program if it is a runnable script. Otherwise, 
# it's a simple module that one is a file containing Python definitions and 
# statements.    
if __name__ == '__main__':
   print ( 'Script\'s name: %s' % os.path.basename(__file__) )
   print ( 'Call print_all() from module shellenv:' )
   # print all variables in SHELL:  
   shellenv.print_all()
