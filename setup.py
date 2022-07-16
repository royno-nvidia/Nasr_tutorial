import setuptools
from setuptools import setup
requires_modules = [
        'argparse',
        'pydriller',
        'xlsxwriter',
        'datetime'
        ]

setup(
    name='pythonProject4',
    version='1.0.0',
    install_requires=requires_modules,
    packages=setuptools.find_packages(),
    url='https://github.com/nasr-saab/Nasr_tutorial',
    license='',
    author='nasr saab',
    author_email='nsaab@nvidia.com',
    description='Write all the commits in Excel file',
    python_requre='>=3',
    py_modules=['parser_module']
)
