#!/usr/bin/python3
""" Tests for City class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
import models


class TestingCity(unittest.TestCase):
    """ City class - tests """
    def test_City1(self):
        """ Test of the City class """
        my_City1 = City()

    def test_City2(self):
        """ Test of the City class """
        my_City2 = City(1)
        my_City3 = City("hola")
        my_City4 = City([1, 2, 3])
        my_City5 = City({"hola": "chau"})

    def test_City3(self):
        """ Test of the City class """
        self.assertEqual(str(type(City)), "<class 'type'>")

    def test_City4(self):
        """ Test of the City class """
        my_City6 = City()
        self.assertEqual(isinstance(my_City6, City), True)

    def test_City5(self):
        """ Test of the City class """
        my_City7 = City()
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_City6(self):
        """ Test of the City class """
        self.assertEqual(issubclass(City, FileStorage), False)

    def test_City7(self):
        """ Test of the City class """
        my_City8 = City()
        my_City8.state_id = "Colorado"
        my_City8.name = "Denver"
        self.assertEqual(str(type(my_City8.state_id)), "<class 'str'>")
        self.assertEqual(my_City8.state_id, "Colorado")
        self.assertEqual(str(type(my_City8.name)), "<class 'str'>")

    def test_City8(self):
        """ Test of the City class """
        my_City9 = City()
        my_City9.state_id = "Borussia"
        my_City9.name = "Dortmund"
        self.assertTrue("state_id" in my_City9.__dict__)
        self.assertTrue("name" in my_City9.__dict__)

    def test_City9(self):
        """ Test of the City class """
        my_City10 = City()
        self.assertFalse("first" in my_City10.__dict__)

    def test_City10(self):
        """ Test of the Amenity class """
        my_City11 = City()
        self.assertEqual(str(type(my_City11.id)), "<class 'str'>")

if __name__ == "__main__":
    unittest.main()
