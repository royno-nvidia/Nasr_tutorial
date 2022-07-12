import setuptools
from setuptools import setup, find_packages
# read the contents of your README file
# from os import path
# this_directory = path.abspath (path.dirname (__file__))
# with open (path.join (this_directory , 'README. md'), encoding ='utf-8') as f:
#     long_description = f.read


setup(
    name='myPythonProject',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pydriller',
        'xlsxwriter'
    ],
    python_requires='>=3.10.5',
    url='https://github.com/nasr-saab/Nasr_tutorial/new/main',
    license='',
    author='nasrsaab',
    author_email='nasr.saab@gmail.com',
    description='git commit from the web sit and show it in the command line',
    py_modules=['parser_module'],

)
