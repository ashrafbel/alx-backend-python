#!/usr/bin/env python3
"Parameterize a unit test"

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Tuple, Union, Dict
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests for the `access_nested_map` function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
