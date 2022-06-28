import io
import os
import re
import codecs

from setuptools import setup, find_packages

def read(filename, encoding='utf-8'):
    """read file contents"""
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with io.open(full_path, encoding=encoding) as fh:
        contents = fh.read().strip()
    return contents

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
        name = "shellenv",
        version=get_version('src/shellenv/__init__.py'),
        url = 'https://github.com/rjaan/python-shellenv.git',
        license = 'PSF',
        description = "You able to operate SHELL's enviroment variables",
        author = 'Andrey Rzhavskov',
        packages=find_packages(where='src',exclude=["shellenv-tools"]),
        package_dir={
                 '': 'src',
        }, 
        install_requires = [ 'setuptools>=42', 'python-dotenv>=0.19' ],
        python_requires = '>=3.8',
        long_description=read('README.md'),
        classifiers=[
            "Programming Language :: Python :: 3",
            "OSI Approved::Python Software Foundation License",
            "Operating System :: OS Independent"
            # Get strings from
            # http://pypi.python.org/pypi?%3Aaction=list_classifiers
            ],
        zip_safe=True,
        include_package_data = False, 
        entry_points={
            "console_scripts": ["py-shellenv=shellenv.__main__:main"],
        },
        options={"bdist_wheel": {"universal": True}},
        platforms=["any"],
)
