#!/usr/bin/env python3

import os
import shellenv

__sherryhw = 'Sherry platform'

def __run_printall()->bool:
    """ print all variables in SHELL:"""
    print ( '\t*** Print all environment variables ***' )  
    if shellenv.print_all(silently=True) == 0 :
       return False
    return True

def __run_scanforhits()->bool:
    print ( '\t*** Scans for hits ***' )
    (key,pos)=shellenv.nmaxhitsenv('SHERRYHW_NAME')
    if key == '' :    
       return False
    print ( '\t' +str(key)+':'+str(pos)+' may be a maximum compliance with: SHERRYHW_NAME' )   
    (key,pos)=shellenv.nminhitsenv('SHERRYHW_NAME')
    if key == '' :    
       return False
    print ( '\t'+str(key)+':'+str(pos)+' may be a minimum compliance with: SHERRYHW_NAME' )   
    return True

def __run_setenv()->bool:
    """
    add new varaible SHERRYHW_NAME with value 'Sherry platform' :
    """
    if ( shellenv.setenv('SHERRYHW_NAME',__sherryhw) == True and 
                            __sherryhw != shellenv.getenv('SHERRYHW_NAME') ) :
       return False 
    return True

def __run_unsetenv()->bool:   
    """
      try to delete varaible's named MYVAR
    """ 
    print ( '\t *** test to unsetenv() when envar does not exists ***' )
    if shellenv.unsetenv('\tMYVAR') != None :
       print ( '\tFAILURE' )
       return False     
    print ('\t Sure, MYVAR\'s does not exists - it\'s right')  
    print ( '\t *** test to unsetenv() test to unsetenv() to removes SHERRYHW_NAME ***' )
    v=shellenv.unsetenv('SHERRYHW_NAME')
    if v == None :
       print ( '\tFAILURE' )
       return False       
    print ( '\t It was not unexpected that SHERRYHW_NAME had the value \'%s\'' % (v,) )  
    return True

def __run_dotenv()->bool:   
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
       return True
    except:
           return False
           pass

def functionality_check()->bool:
   """
      This function is a major and it will run other functions into the location
   """
   print ( 'Script\'s name: %s' % os.path.basename(__file__) )

   print ( 'Call print_all() from module shellenv:' )
   if __run_printall() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )

   print ( 'Call nmaxhitsenv()/nminhitsenv() from module shellenv:' )
   if __run_scanforhits() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )
   
   print ( 'Call setenv(\'SHERRYHW_NAME\') from module shellenv:' )
   if __run_setenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   print ( 'Call run_unsetenv(\'MYVAR\' and \'SHERRYHW_NAME\') from module shellenv:' )
   if __run_unsetenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   print ( 'Call dotenv from module shellenv:' )
   if __run_dotenv() == False: 
      print ( 'FAILURE' ) 
      return False
   print ( 'PASSED' )   

   return True

