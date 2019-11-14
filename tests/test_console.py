#!/usr/bin/env python3
'''test for console'''
import unittest
import pep8
import console
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


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
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        '''test create command input'''
        array_strings = ["** class name missing **",
                         "** class doesn't exist **"]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(array_strings[0]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create NotexistThisClass")
            self.assertEqual(array_strings[1]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            print(self.consol.onecmd("all User"))
            self.assertEqual("[User]", f.getvalue()[2:8])

    def test_destroy(self):
        '''test destroy command input'''
        array_strings = ["** class name missing **",
                         "** class doesn't exist **",
                         "** instance id missing **",
                         "** no instance found **"]

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(array_strings[0]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy NotExistThisClass")
            self.assertEqual(array_strings[1]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy State")
            self.assertEqual(array_strings[2]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 12345")
            self.assertEqual(array_strings[3]+'\n', f.getvalue())

    def test_all(self):
        array_strings = ["** class doesn't exist **", "[]"]
        '''test all command input'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all NotExistThisClass")
            self.assertEqual(array_strings[0]+'\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all City")
            self.assertEqual(array_strings[1]+'\n', f.getvalue())

    def test_update(self):
        '''test update command input'''
        array_strings = ["** class name missing **",
                         "** class doesn't exist **",
                         "** instance id missing **",
                         "** no instance found **",
                         "** attribute name missing **",
                         "** value missing **"]

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual(array_strings[0]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update NotExistThisClass")
            self.assertEqual(array_strings[1]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User")
            self.assertEqual(array_strings[2]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User 12345")
            self.assertEqual(array_strings[3]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            obj = f.getvalue()

        my_id = obj[obj.find('(')+1:obj.find(')')]

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + my_id)
            self.assertEqual(array_strings[4]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + my_id + " Name")
            self.assertEqual(array_strings[5]+'\n', f.getvalue())

    def test_emptyline(self):
        '''test empty line input'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('\n')
            self.assertEqual('', f.getvalue())

    def tes_wrong_command(self):
        '''Test command not immplented'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("command")
        stdout = f.getvalue().strip()
        expetcted = "*** Unknown syntax: command"
        self.assertIn(expetcted, stdout)

    def test_help_tester(self):
        ''' test help '''
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  create  destroy  help  quit  show  update\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        stdout = f.getvalue()
        self.assertIn(expected, stdout)

    def test_show(self):
        '''Test the show function'''
        array_strings = ["** class name missing **",
                         "** class doesn't exist **",
                         "** instance id missing **",
                         "** no instance found **"]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(array_strings[0]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show NotExistThisClass")
            self.assertEqual(array_strings[1]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show User")
            self.assertEqual(array_strings[2]+'\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User 12345")
            self.assertEqual(array_strings[3]+'\n', f.getvalue)

if __name__ == "__main__":
    unittest.main()
