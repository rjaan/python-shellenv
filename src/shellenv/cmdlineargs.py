#Author: Andrey Rzh(Rj)avskov a.k.a rjaan
#E-mail: rjaan@yandex.ru

import os
import sys
import argparse
import typing as t

from .testrun import functionality_check
from shellenv import __version__, print_all, nmaxhitsenv, getenv, similarvars_nhitsenv    
"""
    Defining the derivative classes from argparse.Action    
"""
class _CommonAction(argparse.Action):
      """
          Defining the Common Action to set an option handler 
      """
      def __init__(self, catcher, **kwargs ) :
          option_strings=self._kwargs_get(kwargs,'option_strings')
          dest=self._kwargs_get(kwargs,'dest') 
          nargs=self._kwargs_get(kwargs,'nargs')
          if nargs is None :
             nargs = 0
          if self._kwargs_get(kwargs,'help') is None :
             raise argparse.ArgumentTypeError("help value must always be assigned!")
          if self._kwargs_get(kwargs, 'required') is None :
             raise argparse.ArgumentTypeError("required value must always be define explisity, True or False!")
          super(_CommonAction, self).__init__(
                        option_strings=option_strings, dest=dest, nargs=nargs, help=kwargs['help']
                      ) 
          self.catcher=catcher
 
      @staticmethod
      def _kwargs_get(kws,key): 
          for k in kws.keys():
               if k == key :
                  return kws[k]
          return None

      @classmethod
      def catcher(cls, **kwargs ) :
          raise argparse.ArgumentTypeError( 'direct call CommonAction.catcher() is illegal!' ) 

      def __call__(self, parser, namespace, values, option_string=None):
          #print('Run option: namespace=%r, values=%r, option_string=%r' % (namespace, values, option_string))
          setattr(namespace, self.dest, values)
          if not self.catcher is None :
             sys.exit(self.catcher (
                                     option_string=option_string,  namespace=namespace, values=values 
				   ) 
                     )
          sys.exit(1)

class _TestRunAction(_CommonAction):
      """
          Defining Action for option --test
      """
      def __init__(self, option_strings, dest, nargs=None, **kwargs ):
          super(_TestRunAction, self).__init__( catcher=self.catcher, option_strings=option_strings, dest=dest, nargs=nargs ,**kwargs )
          
      @classmethod
      def catcher(cls, **kwargs ): 
          rval=functionality_check()
          #print ( 'Call TestRunAction: returns zero-value' )
          if rval != 0 :
             return 0 
          return 1 

class _OutputAllRunAction(_CommonAction):
      """
         Defining Action for option --output-all
      """
      def __init__(self, option_strings, dest, nargs=None, **kwargs ):
          super(_OutputAllRunAction, self).__init__( catcher=self.catcher, option_strings=option_strings, dest=dest, nargs=nargs ,**kwargs )
      
      @classmethod
      def catcher(cls, **kwargs ): 
          n=print_all() 
          print ( 'Read %d shell\'s variables' % n )
          if n != 0 :
             return 0 
          return 1
       
class _GetenvAllRunAction(_CommonAction):
      """
         Defining Action for option --getenv vkey|criteria 
      """
      def __init__(self, option_strings, dest, nargs=None, **kwargs ):
          super(_GetenvAllRunAction, self).__init__( catcher=self.catcher, option_strings=option_strings, dest=dest, nargs=nargs ,**kwargs )
      
      @classmethod
      def catcher(cls, **kwargs ): 
          vkey = cls._kwargs_get(kwargs,'values')[0]
          (nvars,similarvars)=similarvars_nhitsenv(vkey)
          if similarvars : 
             print ('There was found '+str(nvars)+' similar variables that start with an '+vkey )
             for key in similarvars.keys() :
                 print('{}={}'.format( key, similarvars.get(key) ) )             
             sys.exit(0)

          (key,pos)=nmaxhitsenv(vkey)
          if len(key) - len(vkey) == 0 :
             print('{}={}'.format( vkey, getenv(vkey) ) )
             sys.exit(0)
          else :         
             sys.exit(1)
 
def mloop_exec(self,argv: t.Sequence[str] = None)->None:
    """
    This function may be run by according to next help page:
    
    ./shellenv [options]     

    Options:
              --help           returns help page and exit immediate)
              --version        prints a version and an info about creater module 
              -t,--test-all    tests all methods for functionality checking
              -O,--output-all  output all of shell enviroment variables
              --getenv vkey    finds and prints all shell variables with keyword 
                               or only one variable when it has matched vkey      
    """
    if argv is None:
       # argv[0] is the script name so we may be skip it and start from 
       # first item  
       argv = sys.argv[1:]
    
    parser = argparse.ArgumentParser(prog='shellenv', usage='%(prog)s [options]')
    # Unessential option                   
    parser.add_argument(
                     "-V","--version",
                     action="version",
                     version=str('The %(prog)s'+'-'+__version__),
                     help=str("returns help page and exit immediate")
    )
    parser.add_argument(
                     "-t","--test",
                     required=False,
                     help=str("tests all methods for functionality checking"),
                     action=_TestRunAction 
    )
    parser.add_argument(
                     "-O","--output-all",
                     required=False,
                     help=str("output all of shell enviroment variables"),
                     action=_OutputAllRunAction
    )
    parser.add_argument("--getenv",
                        nargs=1,
                        required=False,
                        help=str("""finds and prints all shell variables on its keyword
                                    or only one variable when it has matched vkey"""),
                        action=_GetenvAllRunAction 
    )
                                      
    #   
    # Ah, required options don't have used here. So, while I can not find 
    # reasons to be used them.
    #    
    args = parser.parse_args(argv)
    parser.print_help()
    sys.exit(1) # Unix programs generally use 1 for all other kind of errors  
                # than it is. In doing so, returned zero-value is a successful 
                # completion of the module

