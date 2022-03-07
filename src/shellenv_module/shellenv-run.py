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
   print ( '*** Print all environment variables ***' )  
   if shellenv.print_all() == 0 :
      print ( 'FAILURE' ) 
      sys.exit(False)
  
   # scannig the environment variables how accurate to coincided a compared variable 
   # name per characters.
   print ( '*** Scans for hits ***' )
   (key,pos)=shellenv.nmaxhitsenv('SHERRYHW_NAME')
   if key == '' :    
      print ( 'FAILURE' ) 
      sys.exit(False)
   print ( str(key)+':'+str(pos)+' may be a maximum compliance with: SHERRYHW_NAME' )   
   (key,pos)=shellenv.nminhitsenv('SHERRYHW_NAME')
   if key == '' :    
      print ( 'FAILURE' ) 
      sys.exit(False)
   print ( str(key)+':'+str(pos)+' may be a minimum compliance with: SHERRYHW_NAME' )   

   # add new varaible SHERRYHW_NAME with value 'Sherry platform' :
   print ( '*** test setenv()/getenv() ***' )
   shellenv.setenv('SHERRYHW_NAME',sherryhw) 
   sherryhw = shellenv.getenv('SHERRYHW_NAME')
   if ( sherryhw != 'Sherry platform' ) :
     print ( 'FAILURE' ) 
     sys.exit(False)

   print ( 'Ok, set up / changed value \'%s\'' % (sherryhw,) )

   # try to delete varaible's named MYVAR 
   print ( '*** test to unsetenv() when envar does not exists ***' )
   if shellenv.unsetenv('MYVAR') != None :
      print ( 'FAILURE' )   
   print ('Sure, MYVAR\'s does not exists - it\'s a true')  
   print ( '*** test to unsetenv() test to unsetenv() to removes SHERRYHW_NAME ***' )
   v=shellenv.unsetenv('SHERRYHW_NAME')
   if v == None :
      print ( 'FAILURE' )       
   print ( 'It was not unexpected that SHERRYHW_NAME had the value \'%s\'' % (v,) )  
   print ( 'DONE.' ) 
   sys.exit(True)

