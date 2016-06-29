"""A setuptools based setup module.

See:
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

import subprocess as sub
import re

# build database
# curl the page with the quotes
curl = sub.Popen(['curl', 'http://morecoolquotes.com/famous-yoda-quotes/'],stdout=sub.PIPE,stderr=sub.PIPE)
content, errors = curl.communicate()

# extract the quotes
quotes = re.findall('<li>([^<]+) &#8211; Yoda</li>', content)

# print db details
print "Constructed database with " + str(len(quotes)) + " quotes."

# write the contents to a file
f = open('dailyyoda/quotes.db', 'w')
for quote in quotes:
  f.write(quote + "\n")
f.close()

# configure installation
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dailyyoda',

    version='0.1.0',

    description='Yoda quote of the day',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/smcrosb/daily-yoda',

    # Author details
    author='Sean Crosby',
    author_email='seancrosby@users.noreply.github.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='example',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    #install_requires=['peppercorn'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
   # extras_require={
   #     'dev': ['check-manifest'],
   #     'test': ['coverage'],
   # },

    # data
    package_data={
        '': ['test.db', 'quotes.db'],
    },

    # entry point
    entry_points={
        'console_scripts': [
            'dailyyoda=dailyyoda:main',
        ],
    },
)
