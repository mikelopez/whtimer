#dev@scidentify.info - Marcos Lopez
import unittest
import sys
import os
sys.path.append('../')
from termprint import *
from db import Database

class BaseTest(unittest.TestCase):
    def add_task(self, name):
        """Adds a task to test timer functionality"""
        pass
