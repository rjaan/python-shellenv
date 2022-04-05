#!/usr/bin/env python3

"""shellenv.py: Using the module shellenv, you able to operate with environment variables"""

import os          
from typing import ( List, Dict, Tuple,TypedDict )

def unsetenv(key: str) -> str :   
    """ removes the variable name from os.environ """
    return os.environ.pop(key,default=None)
     
def setenv(newkey: str, newvalue: str) -> bool : 
    """ either change an exists key or append new key to dictionary """
    if not os.environ.get(newkey):
       os.environ.setdefault(newkey,newvalue)
       return True;
    return changenv(vkey,newvalue);

class DictKHints(TypedDict):
      """ 
          This class is a dictionary objects with a specific set of string keys

          key   -- variable key has the string type that
          value -- allow to avoid problem to extract their values
      """ 
      key:str    # variable key has the string type that   
      value:str  # allow to avoid problem to extract their values  
      
class KHints():      
     """ 
     I needed to create the class where a problem will be resolved when  
     the nested dictionary list scans to get maximum number of hits in this

     Why you can't inherit Python built-in dict type,
     see to http://www.kr41.net/2016/03-23-dont_inherit_python_builtin_dict_type.html
     """    
     def __init__(self)->None:
         self.dkeys=DictKHints()
         
     def __gethits(self,k:str)->int : 
         (h,p)=self.dkeys.get(k)
         return h

     def domax(self)->str :
         return max(self.dkeys,key=self.__gethits) 

     def domin(self)->str :
         return min(self.dkeys,key=self.__gethits) 

     def dosimilarvars(self,ckey:str)->Tuple[int,TypedDict]:
         nvars=0
         for k in os.environ.keys() :
            if k[0:len(ckey)] == ckey :
               if len(k) == len(ckey) :
                  return (0,None) 	
               self.dkeys.update({k:getenv(k)})                	           
               nvars+=1
         if nvars :
            return (nvars,self.dkeys)                      
         return (0,None)

def __nhitsenv(ckey: str) -> KHints:
     """
     scans an environment variables how accurate to coincided 
     a compared variable name per characters.
     """
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
     return pkeys;

def similarvars_nhitsenv (criteria: str)->Tuple[int,TypedDict]:
    """
    search multiple variables and their values on first characters in 
    the variable name  that have to start from the same name as desired variables.     
    """ 
    return KHints().dosimilarvars(criteria)
    
def nmaxhitsenv(ckey : str) -> Tuple[str,int]:
    """
    This function returns two values. The first to be returned a value of max number 
    was fell out at time of symbol matching. And the second is coming next 
    a position into os.environ where it occured.   
    """
    pkeys=__nhitsenv(ckey)
 
    if len(pkeys.dkeys) :
       __maxhave_k=pkeys.domax()
       (h,p)=pkeys.dkeys.get(__maxhave_k) 
       return (__maxhave_k,p)
    return ('',0)   

def nminhitsenv(ckey) -> Tuple[str,int]:
    """
    This function does the same as  nmaxhitsenv() but it returned a value of 
    min number was fell out at time of symbol matching.
    """
    pkeys=__nhitsenv(ckey) 
    if len(pkeys.dkeys) :
       __minhave_k=pkeys.domin()
       (h,p)=pkeys.dkeys.get(__minhave_k) 
       return (__minhave_k,p)
    return ('',0)   

def changenv(vkey: str, newvalue: str ) -> bool:
    """
    the function updates os.environ to modify since calling os.putenv() 
    does not affect it.
     - * vkey     *: a variable name as dictionary key and     
     - * newvalue *: had updated to it. 
    """    
    for key, value in os.environ.items():
       if vkey == key : 
          os.environ.update([(vkey,newvalue)])           
          return True
       return False 

def getenv(vkey) -> str:
    """
    The function getenv(vkey) is an analog of C-function GETENV(3). It searches a 
    variable value into os.environ on the variable key. And then it returns this 
    value if such key has been found. Otherwise an empty text is returned 
    if nothings has been found.  
    - * ckey     *: contains a variable name as to use as a dictionary key for                     
    """ 
    for key, value in os.environ.items():
       if vkey == key : 
          return value
    return "" # an empty text if nothings has been found   

def print_all(ckey: str ='ENVALL', silently: bool = False) -> int:
    """ 
    The function print_all is an analog of shell-command ENV(1).
    Actually, print all environment variables on the standard output if those 
    variables is accessible to Python. However, when ckey does not match ENVALL, 
    only one key to be printed if it will be found, sure.
      - *dotenv_path*: when this does not match ENVALL only one key to be printed 
                       if they will be found in os.environ 
      - *  silently *: the function returns the number of detected keys which 
                       will be read in os.environ             
    """
    n=int(0)       
    for key in os.environ:
      if silently == False :  
         print('{}={}'.format(key, getenv(key)))  
      n+=1
      if ckey != 'ENVALL' and key == ckey :   
         return n
    return n

