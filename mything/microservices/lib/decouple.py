# coding: utf-8
# MIT License - https://github.com/henriquebastos/python-decouple
import os
import sys
import string
from shlex import shlex
from io import open
from collections import OrderedDict
from distutils.util import strtobool

# Useful for very coarse version differentiation.
PY3 = sys.version_info[0] == 3

if PY3:
    from configparser import ConfigParser
    text_type = str
else:
    from ConfigParser import SafeConfigParser as ConfigParser
    text_type = unicode

DEFAULT_ENCODING = 'UTF-8'

class UndefinedValueError(Exception):
    pass


class Undefined(object):
    """
    Class to represent undefined type.
    """
    pass


# Reference instance to represent undefined values
undefined = Undefined()


class Config(object):
    """
    Handle .env file format used by Foreman.
    """

    def __init__(self, repository):
        self.repository = repository

    def _cast_boolean(self, value):
        """
        Helper to convert config values to boolean as ConfigParser do.
        """
