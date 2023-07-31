#!/usr/bin/env python3
"""Unit test for utils.py"""


import unittest
from utils import access_nested_map
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


if __name__ == "__main__":
    unittest.main()
