[![Build Status](https://travis-ci.org/OrangeTux/python-snake.svg?branch=develop)](https://travis-ci.org/OrangeTux/python-snake)

# Snake
A minimal implementation of Snake in Python.

# Installation
Create a virtualenv and install the requirements

## Python 2.7

    $ virtualenv .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

## Python 3.3
    
    $ pyvenv-3.3 .env
    $ source .env/bin/activate
    $ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ python get-pip.py
    # I need to reactivate the virtualenv
    $ deactivate
    $ source .env/bin/activate
    $ pip install -r requirements.txt

# Usage
Run Snake with:

    ./snake.py

Run the test suite with:

    py.test tests
