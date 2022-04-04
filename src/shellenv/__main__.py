#!/usr/bin/env python3

""" shellenv-run.py: tests Python's module python-shellenv to display enviroment info"""

import typing as t
from .cmdlineargs import mloop_exec

"""
   This module python-shellenv runs command next as
 
      $ python3 -m 

   Or executes wrapper script in command line by
      
      $ py-shellenv

   And how it was written in setup.py  
"""
     
def main(argv: t.Sequence[str] = None)->None:
    """ 
       This function allows to call some method of whose application is 
       justifiable in command line.

       Namely, following methods can be used in command line, such as

       print_all()    prints all variable values from os.environ
       getenv(vkey)   searches a variable value into os.environ and then it returns 
                      this value if such vkey has been found.                  
       functionality_check() runs all methods for functionality testing  

       And those methods are actually to use, in my view.   
    """ 
    mloop_exec(argv)

if __name__ == '__main__':
   main()

