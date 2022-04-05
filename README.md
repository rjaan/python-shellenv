# (python-)shellenv is python's module to operate with environment variables   

  **shellenv(_module)** is python's module to display enviroment info and 
  it's consisting of two files written on Python. Both files may use as either 
  an executed script or included module.

  Using the module shellenv, you able to operate environment variables with
  use equivalents to the functions family getent(3) in C

  **unsetenv(vkey)**: removes variable key from os.environ

  **getenv(vkey)**: searches a value into os.environ and then it returns this 
    value if such vkey has been found.

  **setenv(newkey,newvalue)**: either change an exists key or append new key to dictionary.

  **print_all()**: prints all value from os.environ and counts total numbers vkeys

  **similarvars_nhitsenv()**: search multiple variables and their values by 
    first characters in the variable name that have to start from the same name as desired variables
  
  First, you get a source code of this module and go to the directory python-shellenv, as below.
```   
    $ git clone https://github.com/rjaan/python-shellenv.git && \
      cd python-shellenv
```
  And then build python-shellenv, you have to run following command in the repo directory:
``` 
    $ python -m build
```
  Finally, you need to install this module from your local PIP or run the next command:
```
    $ pip install shellenv_module-rjaan-1.5.tar.gz 
```
  The module python-shellenv runs command next as
``` 
    $ python3 -m 
```
  Or executes wrapper script in command line by
```      
    $ py-shellenv
```
  You have to run py-shellenv with option --help to get detailed information of use it
```    
   $ ../../bin/py-shellenv --help
   usage: shellenv [options]

   optional arguments:
          -h, --help        show this help message and exit
          -V, --version     returns help page and exit immediate
          -t, --test        tests all methods for functionality checking
          -O, --output-all  output all of shell enviroment variables
          --getenv GETENV   finds and prints all shell variables on its keyword or 
                            only one variable when it has matched vkey
```
 For version 1.6 of the module py-shellenv, it released a feature to search 
 the multiple environment variables and their actual values by first characters in 
 the variable name. This  feature runs via option --getenv, e.g 
```
   $ py-shellenv --getenv SSH
   There was found 2 similar variables that start with an SSH
   SSH_AGENT_LAUNCHER=openssh
   SSH_AUTH_SOCK=/run/myuser/1103/keyring/ssh
```
This project is licensed under the Python Software Foundation License Version 2.

