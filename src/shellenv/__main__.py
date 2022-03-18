#!/usr/bin/env python3

""" shellenv-run.py: tests Python's module python-shellenv to display enviroment info"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import sys

__sherryhw = 'Sherry platform'
"""
   We will run the module as program if it is a runnable script. Otherwise, 
   it's a simple module that one is a file containing Python definitions and 
   statements.    
"""
def run_printall()->bool:
    """ print all variables in SHELL:"""
    print ( '\t*** Print all environment variables ***' )  
    if print_all() == 0 :
       return False
    return True

def run_scanforhits()->bool:
    print ( '\t*** Scans for hits ***' )
    (key,pos)=nmaxhitsenv('SHERRYHW_NAME')
    if key == '' :    
       return False
    print ( '\t' +str(key)+':'+str(pos)+' may be a maximum compliance with: SHERRYHW_NAME' )   
    (key,pos)=nminhitsenv('SHERRYHW_NAME')
    if key == '' :    
       return False
    print ( '\t'+str(key)+':'+str(pos)+' may be a minimum compliance with: SHERRYHW_NAME' )   
    return True

def run_setenv()->bool:
    """
    add new varaible SHERRYHW_NAME with value 'Sherry platform' :
    """
    if ( setenv('SHERRYHW_NAME',__sherryhw) == True and 
                            __sherryhw != getenv('SHERRYHW_NAME') ) :
       return False 
    return True

def run_unsetenv()->bool:   
    """
      try to delete varaible's named MYVAR
    """ 
    print ( '\t *** test to unsetenv() when envar does not exists ***' )
    if unsetenv('\tMYVAR') != None :
       print ( '\tFAILURE' )
       return False     
    print ('\t Sure, MYVAR\'s does not exists - it\'s right')  
    print ( '\t *** test to unsetenv() test to unsetenv() to removes SHERRYHW_NAME ***' )
    v=unsetenv('SHERRYHW_NAME')
    if v == None :
       print ( '\tFAILURE' )
       return False       
    print ( '\t It was not unexpected that SHERRYHW_NAME had the value \'%s\'' % (v,) )  
    return True

def run_dotenv()->bool:   
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
       print('SHELLENV_DIR: %s' % getenv('SHELLENV_DIR') )
       print('DOMAIN: %s' % getenv('DOMAIN') )
       print('USER_EMAIL: %s' % getenv('USER_EMAIL') )  
       os.remove(dotenvpath)    
       os.rmdir(os.environ['HOME']+dotenvdir) 
       return True
    except:
           return False
           pass

def functionality_check(argv=None)->None:
   """
      This function is a major and it will run other functions into the location
   """
   print ( 'Script\'s name: %s' % os.path.basename(__file__) )

   print ( 'Call print_all() from module shellenv:' )
   if run_printall() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )

   print ( 'Call nmaxhitsenv()/nminhitsenv() from module shellenv:' )
   if run_scanforhits() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )
   
   print ( 'Call setenv(\'SHERRYHW_NAME\') from module shellenv:' )
   if run_setenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   print ( 'Call run_unsetenv(\'MYVAR\' and \'SHERRYHW_NAME\') from module shellenv:' )
   if run_unsetenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   print ( 'Call dotenv from module shellenv:' )
   if run_dotenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   return True
   
if __name__ == '__main__':
       sys.exit(functionality_check())

#   sherryhw = 'Sherry platform'
#   print ( 'Script\'s name: %s' % os.path.basename(__file__) )
#   print ( 'Call print_all() from module shellenv:' )
#   """ print all variables in SHELL:"""
#   print ( '*** Print all environment variables ***' )  
#   if shellenv.print_all() == 0 :
#      print ( 'FAILURE' ) 
#      sys.exit(False)
#   """
#     scannig the environment variables how accurate to coincided a compared variable 
#     name per characters.
#   """
#   print ( '*** Scans for hits ***' )
#   (key,pos)=shellenv.nmaxhitsenv('SHERRYHW_NAME')
#   if key == '' :    
#      print ( 'FAILURE' ) 
#      sys.exit(False)
#   print ( str(key)+':'+str(pos)+' may be a maximum compliance with: SHERRYHW_NAME' )   
#   (key,pos)=shellenv.nminhitsenv('SHERRYHW_NAME')
#   if key == '' :    
#      print ( 'FAILURE' ) 
#      sys.exit(False)
#   print ( str(key)+':'+str(pos)+' may be a minimum compliance with: SHERRYHW_NAME' )   
#   """
#    add new varaible SHERRYHW_NAME with value 'Sherry platform' :
#   """
#   print ( '*** test setenv()/getenv() ***' )
#   shellenv.setenv('SHERRYHW_NAME',sherryhw) 
#   sherryhw = shellenv.getenv('SHERRYHW_NAME')
#   if ( sherryhw != 'Sherry platform' ) :
#     print ( 'FAILURE' ) 
#     sys.exit(False)
#
#   print ( 'Ok, set up / changed value \'%s\'' % (sherryhw,) )
#   """
#     try to delete varaible's named MYVAR
#   """ 
#   print ( '*** test to unsetenv() when envar does not exists ***' )
#   if shellenv.unsetenv('MYVAR') != None :
#      print ( 'FAILURE' )   
#   print ('Sure, MYVAR\'s does not exists - it\'s a true')  
#   print ( '*** test to unsetenv() test to unsetenv() to removes SHERRYHW_NAME ***' )
#   v=shellenv.unsetenv('SHERRYHW_NAME')
#   if v == None :
#      print ( 'FAILURE' )       
#   print ( 'It was not unexpected that SHERRYHW_NAME had the value \'%s\'' % (v,) )  
#   """ test an external module python-dotenv to read enviroment values from a dotfile """
#   try:
#      from dotenv import load_dotenv
#      print ( '*** test to read file [${HOME}/.config/shellenv/].env  ***' )
#      dotenvdir  = '/.config/shellenv/'
#      dotenvpath = os.environ['HOME']+dotenvdir+'.env'
#      if os.path.isdir(dotenvdir) == False :
#       print('Create tested directory: %s' % (dotenvdir,))
#       os.mkdir(os.environ['HOME']+dotenvdir)
#      if os.path.isfile(dotenvpath) == False :
#       print('Create tested dotfile: %s' % (dotenvpath,))
#      with open(dotenvpath, "w") as text_file:
#         print("{}={}".format ( 'SHELLENV_DIR',dotenvdir ), file=text_file)  
#         print("{}={}".format ( 'DOMAIN','localhost'), file=text_file)   
#         print("{}={}".format ( 'USER_EMAIL',os.environ['USER']+'@'+'${DOMAIN}'), file=text_file)
#      load_dotenv(dotenv_path=dotenvpath,verbose=True,encoding = "utf-8")
#      print('Try to read recently recorded envars:')  
#      print('SHELLENV_DIR: %s' % shellenv.getenv('SHELLENV_DIR') )
#      print('DOMAIN: %s' % shellenv.getenv('DOMAIN') )
#      print('USER_EMAIL: %s' % shellenv.getenv('USER_EMAIL') )  
#      os.remove(dotenvpath)    
#      os.rmdir(os.environ['HOME']+dotenvdir) 
#   except:
#          print ( 'FAILURE.' )
#          sys.exit(False)     
#          pass
#
#   print ( 'DONE.' ) 
#   sys.exit(True)

