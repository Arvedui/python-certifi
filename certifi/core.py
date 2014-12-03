#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""

import os
import sys

def where():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'cacert.pem')
    else:
        f = os.path.split(__file__)[0]
        return os.path.join(f, 'cacert.pem')

if __name__ == '__main__':
    print(where())
