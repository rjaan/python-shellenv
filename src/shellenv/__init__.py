
__author__      = "Andrew Rzhaskov"
__copyright__   = "Copyright 2022, Russia Moscow"
__version__      = "1.5" 

from typing import Any, Optional

from .shellenv import ( unsetenv, setenv, getenv, nmaxhitsenv, nminhitsenv, changenv, print_all )
from .testrun import ( functionality_check )

all = [ 'unsetenv',
        'setenv',
        'getenv',
        'nmaxhitsenv',
        'nminhitsenv',
        'changenv',
        'print_all', 
        'functionality_check' ]

# eof

