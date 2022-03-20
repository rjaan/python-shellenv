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
  
  First, you get a source code of this module and go to the directory python-shellenv, as below.
```   
   git clone https://github.com/rjaan/python-shellenv.git &&\
   cd python-shellenv
```
  And then build python-shellenv, you have to run following command in the repo directory:
``` 
   python -m build
```
  Finally, you need to install this module from your local PIP or run the next command:
```
   pip install shellenv_module-rjaan-1.4.tar.gz 
```
Example for using
```
$ python3 -m shellenv
```

This project is licensed under the Python Software Foundation License Version 2.

