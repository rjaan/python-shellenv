#!/usr/bin/env python3

"""shellenv.py: imported module what displays enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import bisect 

#
# The function insrtenva(newkey,newvalue) allows to insert new variable in 
# sorted order
def insrtenva(newkey,newvalue):
    for key, value in os.environ.items():
           

#
# The function changenv(vkey,newvalue) updates os.environ to modify since  
# calling os.putenv() directly since calling the function does nothing 
# affect to os.environ .    
#
def changenv(vkey,newvalue):
    for key, value in os.environ.items():
       if vkey == key : 
          os.environ.update([(vkey,newvalue)])           
          return True
       return False 

# The function getenv(vkey) is an analog of C-function GETENV(3). It finds a 
# variable value into os.environ on the variable key. And then it returns this 
# value if such key has been found. 
# 
def getenv(vkey):
    for key, value in os.environ.items():
       if vkey == key : 
          return value
    return "" # an empty text if nothings has been found   

#
# the function print_all is an analog of shell-command ENV(1)
# 
def print_all():
    print ( '*** Print all environment variables ***' )
# Actually, print all environment variables on the standard output if those 
# variables is accessible to Python .       
    for key in os.environ:
       print('{}={}'.format(key, getenv(key)))  

