import io
import os
import re
from setuptools import setup, find_packages
from setuptools.config import read_configuration

def read_config( vkey ): 
    """
    Read given configuration file from root directoty and returns options from 
    it as a dict. 
    """
    conf_dict = read_configuration(os.path.dirname(os.path.abspath(__file__))+'/'+'setup.cfg' )

    return conf_dict.get('metadata')[vkey] 
 
def read(filename, encoding='utf-8'):
    """read file contents"""
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with io.open(full_path, encoding=encoding) as fh:
        contents = fh.read().strip()
    return contents

def get_package_version():
    """get version from top-level package init"""
    version_file = read('src/shellenv/__init__.py')
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)

    """if you didn't able to read nothing from top-level package init,
       you should try to get the version from top-level package file setup.cfg 
    """
    version=read_config( 'version' )
    if version == None :
       raise RuntimeError('Unable to find version string.')        
    
    return version       

setup(
        name = "shellenv",
        version=get_package_version(),
        url = 'https://github.com/rjaan/python-shellenv.git',
        license = 'PSF',
        description = "You able to operate SHELL's enviroment variables",
        author = 'Andrey Rzhavskov',
        packages = find_packages('shellenv'),
        package_dir = {'': 'src'},
#        packages = find_packages('shellenv'),
#        package_dir = {'': 'src'},
        install_requires = [ 'setuptools>=42', 'python-dotenv>=0.19' ],
        python_requires  = '>=3.8',
        long_description=read('README.md'),
        classifiers=[
            "Programming Language :: Python :: 3",
            "OSI Approved::Python Software Foundation License",
            "Operating System :: OS Independent"
            # Get strings from
            # http://pypi.python.org/pypi?%3Aaction=list_classifiers
            ],
        zip_safe=True,
        entry_points={
            "console_scripts": ["py-shellenv=shellenv.__main__:main"],
        },
        options={"bdist_wheel": {"universal": True}},
        platforms=["any"],
)
