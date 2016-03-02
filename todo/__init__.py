# -*- coding: utf-8 -*-

from .utils import print_info, Utils

# Do not run any poluting code in __init__:
# This is just a demostration.
print('Runned __init__.py, __name__ = ', __name__)
print_info()
Utils()