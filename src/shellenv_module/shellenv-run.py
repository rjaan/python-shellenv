#!/usr/bin/env python3

"""myscripts.py: execute python code to display enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import sys
import shellenv

# We will run the module as program if it is a runnable script. Otherwise, 
# it's a simple module that one is a file containing Python definitions and 
# statements.    
if __name__ == '__main__':
   sherryhw = 'Sherry platform'
   print ( 'Script\'s name: %s' % os.path.basename(__file__) )
   print ( 'Call print_all() from module shellenv:' )
   # print all variables in SHELL:  
   #shellenv.print_all()
  
   # scannig the environment variables how accurate to coincided a compared variable 
   # name per characters.
   (key,pos)=shellenv.nmaxhitsenv('SHERRYHW_NAME')
   
   print ( str(key)+':'+str(pos)+' may be a maximum compliance with: SHERRYHW_NAME' )   
 
   # add new varaible NEWTEST_MYVAR='New test value':
   shellenv.setenv('SHERRYHW_NAME',sherryhw) 
   sherryhw = shellenv.getenv('SHERRYHW_NAME')
   if ( sherryhw == 'Sherry platform' ) :
     print ( 'test setenv()/getenv() : PASSED' ) 
     sys.exit(True)
   sys.exit(False)            
   

