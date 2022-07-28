import setuptools
from setuptools import setup
requires_modules = [
        'argparse',
        'pydriller',
        'xlsxwriter',
        'datetime',
        'pandas>=1.4.3',
        'xlrd>=1.2.0',
        'openpyxl>=3.0.7'
        ]

setup(
    name='Commit Parser',
    version='1.0.0',
    install_requires=requires_modules,
    packages=setuptools.find_packages(),
    url='https://github.com/nasr-saab/Nasr_tutorial',
    license='',
    author='Nasr Saab',
    author_email='nsaab@nvidia.com',
    description='This python script take all the commits from any Repo that found in any place'
                'locally or remotely and order them in Excel file',
    python_requre='>=3',
    py_modules=['parser_module']
)
