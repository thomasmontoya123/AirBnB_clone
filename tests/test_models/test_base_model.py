#!/usr/bin/python3
'''test for BaseModel'''
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    '''this will test the base model class'''

    @classmethod
    def setUpClass(cls):
        '''setup for the test'''
        cls.base = BaseModel()
        cls.base.name = "Jonathan"
        cls.base.num = 30

    @classmethod
    def teardown(cls):
        '''at the end of the test this will tear it down'''
        del cls.base

    def tearDown(self):
        '''teardown'''
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        '''Testing for pep8'''
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_checking_for_docstring_BaseModel(self):
        '''checking for docstrings'''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        '''chekcing if Basemodel have methods'''
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        '''test if the base is an type BaseModel'''
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        '''test if the save works'''
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_save_without_args(self):
        '''test save without args'''
        with self.assertRaises(TypeError) as e:
            self.base.save()
        expected = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected)

    def test_save_multiple_arguments(self):
        """Test save with more args than expected."""
        with self.assertRaises(TypeError) as e:
            self.base.save(self, 10)
        expected = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), expected)

    def test_to_dict_BaseModel(self):
        '''test if dictionary works'''
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
