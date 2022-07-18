from setuptools import setup, find_packages
import setuptools

setup(
    name='Git_parser_v3',
    version='3.0.0',
    packages=find_packages(),
    install_requires=[
        'pydriller',
        'xlsxwriter',
        'argparse',
        'datetime'
    ],
    url='https://github.com/nasr-saab/Nasr_tutorial',
    license='',
    author='nasr saab',
    author_email='nsaab@nvidia.com',
    description='git parser project'
)
