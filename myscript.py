#!/usr/bin/env python3

"""myscripts.py: execute python code into command-line interface"""

__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"

import os
import mymodule 

class MyScript :
      # constructor for itself	
      def __init__(self,name):
          self.basename = os.path.basename(__file__)
          self.modname  = name
      # print all of shell enviroment variables on standard output
      def env_print(self):
          print ( 'Script\'s name: %s' % os.path.basename(__file__) )
          print ( 'Call shell_env() from %s.py' % self.modname ) 
          mymodule.shell_env()          
                  

# We will run the module as program if it is a runnable script. Otherwise, 
# it's a simple module that one is a file containing Python definitions and 
# statements.    
if __name__ == '__main__':
   MyScript('mymodule').env_print()

