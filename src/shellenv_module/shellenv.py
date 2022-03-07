#!/usr/bin/env python3

"""shellenv.py: Using the module shellenv, you able to operate with environment variables"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os          

# setenv():
# either change an exists key or append new key to dictionary  
def setenv(newkey,newvalue) : 
    if not os.environ.get(newkey):
       os.environ.setdefault(newkey,newvalue)
       return True;
    return changenv(vkey,newvalue);

# I needed to create the class where a problem will be resolved when  
# the nested dictionary list scans to get maximum number of hits in this
# 
# Why you can't inherit Python built-in dict type, 
# see to http://www.kr41.net/2016/03-23-dont_inherit_python_builtin_dict_type.html
class KHints():      
     def __init__(self):
         self.dkeys={}
         
     def __gethits(self,k) : 
         (h,p)=self.dkeys.get(k)
         return h

     def domax(self) :
         return max(self.dkeys,key=self.__gethits) 

# nmaxhitsenv(key) 
#
# scans an environment variables how accurate to coincided 
# a compared variable name per characters.
# This function returns two values. The first to be returned a value of max number 
# was fell out at time of symbol matching. And the second is coming next 
# a position into os.environ where it occured.  
#
def nmaxhitsenv(ckey):
     pkeys=KHints()
     for k in os.environ.keys() :
         nhits=0
         for n in range(1,len(ckey)) :
             if k[0:n] == ckey[0:n] :
                nhits+=1
             pass
         if nhits :
           rpos=list(os.environ.keys()).index(k)
           pkeys.dkeys.update({k:[nhits,rpos]})
     if  len(pkeys.dkeys) :
        maxhave_k=pkeys.domax()
        return (maxhave_k,pkeys.dkeys.get(maxhave_k))
     return ('',0)   
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
# Actually, print all environment variables on the standard output if those 
# variables is accessible to Python.
  n=0       
  for key in os.environ:
      print('{}={}'.format(key, getenv(key)))  
      n+=1
  return n  
