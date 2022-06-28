
__author__      = "Author: Andrew Rzhaskov"
__copyright__   = "Copyright: 2022, Russia Moscow"
__version__      = "1.7" 

from typing import Any, Optional

from .shellenv import ( unsetenv, setenv, getenv, nmaxhitsenv, nminhitsenv, changenv, print_all, similarvars_nhitsenv )

all = [ 'unsetenv',
        'setenv',
        'getenv',
        'nmaxhitsenv',
        'nminhitsenv',
        'changenv',
        'print_all', 
        'functionality_check',
        'similarvars_nhitsenv' ]

# eof

