"""
Provides logging as a decorator

Author: Milton S
"""
import os
import sys
import logging
from pathlib import Path
from datetime import datetime


class Log:

    def __init__(self, function):

        self.function = function

    def __call__(self, *args, **kwargs):

        print("started")
        function = self.function(self, *args, **kwargs)
        print("\nended")
        return function
