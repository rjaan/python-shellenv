#!/usr/bin/env python3

""" shellenv-run.py: tests Python's module python-shellenv to display enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import sys
import shellenv
"""
   We will run the module as program if it is a runnable script. Otherwise, 
   it's a simple module that one is a file containing Python definitions and 
   statements.    
"""
if __name__ == '__main__':
   sherryhw = 'Sherry platform'
   print ( 'Script\'s name: %s' % os.path.basename(__file__) )
   print ( 'Call print_all() from module shellenv:' )
   """ print all variables in SHELL:"""
   print ( '*** Print all environment variables ***' )  
   if shellenv.print_all() == 0 :
      print ( 'FAILURE' ) 
      sys.exit(False)
   """
     scannig the environment variables how accurate to coincided a compared variable 
     name per characters.
   """
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
   """
    add new varaible SHERRYHW_NAME with value 'Sherry platform' :
   """
   print ( '*** test setenv()/getenv() ***' )
   shellenv.setenv('SHERRYHW_NAME',sherryhw) 
   sherryhw = shellenv.getenv('SHERRYHW_NAME')
   if ( sherryhw != 'Sherry platform' ) :
     print ( 'FAILURE' ) 
     sys.exit(False)

   print ( 'Ok, set up / changed value \'%s\'' % (sherryhw,) )
   """
     try to delete varaible's named MYVAR
   """ 
   print ( '*** test to unsetenv() when envar does not exists ***' )
   if shellenv.unsetenv('MYVAR') != None :
      print ( 'FAILURE' )   
   print ('Sure, MYVAR\'s does not exists - it\'s a true')  
   print ( '*** test to unsetenv() test to unsetenv() to removes SHERRYHW_NAME ***' )
   v=shellenv.unsetenv('SHERRYHW_NAME')
   if v == None :
      print ( 'FAILURE' )       
   print ( 'It was not unexpected that SHERRYHW_NAME had the value \'%s\'' % (v,) )  
   """ test an external module python-dotenv to read enviroment values from a dotfile """
   try:
      from dotenv import load_dotenv
      print ( '*** test to read file [${HOME}/.config/shellenv/].env  ***' )
      dotenvdir  = '/.config/shellenv/'
      dotenvpath = os.environ['HOME']+dotenvdir+'.env'
      if os.path.isdir(dotenvdir) == False :
       print('Create tested directory: %s' % (dotenvdir,))
       os.mkdir(os.environ['HOME']+dotenvdir)
      if os.path.isfile(dotenvpath) == False :
       print('Create tested dotfile: %s' % (dotenvpath,))
      with open(dotenvpath, "w") as text_file:
         print("{}={}".format ( 'SHELLENV_DIR',dotenvdir ), file=text_file)  
         print("{}={}".format ( 'DOMAIN','localhost'), file=text_file)   
         print("{}={}".format ( 'USER_EMAIL',os.environ['USER']+'@'+'${DOMAIN}'), file=text_file)
      load_dotenv(dotenv_path=dotenvpath,verbose=True,encoding = "utf-8")
      print('Try to read recently recorded envars:')  
      print('SHELLENV_DIR: %s' % shellenv.getenv('SHELLENV_DIR') )
      print('DOMAIN: %s' % shellenv.getenv('DOMAIN') )
      print('USER_EMAIL: %s' % shellenv.getenv('USER_EMAIL') )  
      os.remove(dotenvpath)    
      os.rmdir(os.environ['HOME']+dotenvdir) 
   except:
          print ( 'FAILURE.' )
          sys.exit(False)     
          pass
 
   print ( 'DONE.' ) 
   sys.exit(True)



