#!/usr/bin/env python3
"""Unit test for utils.py"""


import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized
from typing import Dict, Tuple, Union, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """This class tests access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        result: Union[Dict, int]
            ) -> None:
        """This method runs a test for access_nested_map"""
        returned_element = access_nested_map(nested_map, path)
        self.assertEqual(result, returned_element)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence
    ) -> None:
        """Tests that a key error is returned"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class to test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """The function to test get json"""
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """A test class for the memoize method"""
    def test_memoize(self):
        """The function for the memoize method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(
            TestClass,
            'a_method',
            return_value=42
                ) as mocked_method:
            result = test_instance.a_property
            self.assertEqual(result, 42)
            mocked_method.assert_called_once()
            result = test_instance.a_property
            self.assertEqual(result, 42)
            mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
