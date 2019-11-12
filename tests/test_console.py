#!/usr/bin/env python3
'''test for console'''
import unittest
import pep8
import console
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''setup for the test'''
        cls.consol = HBNBCommand()
    
    def test_pep8_console(self):
        '''test pep8 console.py'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings_in_console(self):
        '''test docstrings console.py'''
        self.assertIsNotNone(console.__doc__)
        array = ["emptyline", "do_quit", "do_EOF", "do_create",
                 "do_show", "do_destroy", "do_all", "do_update",
                 "default"]
        for i in array:
            self.assertIsNotNone(eval("HBNBCommand."+i+".__doc__"))

    def test_quit(self):
        '''test quit command input'''
        pass

    def test_create(self):
        '''test create command input'''
        pass

    def test_destroy(self):
        '''test destroy command input'''
        pass

    def test_all(self):
        '''test all command input'''
        pass

    def test_update(self):
        '''test update command input'''
        pass

    def test_emptyline(self):
        '''test empty line input'''
        pass 
