import json
import os
import unittest
from unittest.mock import patch

from memory.manager import MemoryManager


class TestMemoryManager(unittest.TestCase):

    def test_deep_merge(self):

        old = {
            "name": "Vagish",
            "education": {
                "city": "Bangalore"
            }
        }

        new = {
            "education": {
                "institution": "RNSIT"
            },
            "skills": [
                "Python"
            ]
        }

        result = MemoryManager.deep_merge(old, new)

        self.assertEqual(
            result["name"],
            "Vagish"
        )

        self.assertEqual(
            result["education"]["city"],
            "Bangalore"
        )

        self.assertEqual(
            result["education"]["institution"],
            "RNSIT"
        )

        self.assertEqual(
            result["skills"],
            ["Python"]
        )

    @patch.object(MemoryManager, "load")
    def test_get_all(self, mock_load):

        expected = {
            "name": "Vagish",
            "skills": ["Python"]
        }

        mock_load.return_value = expected

        result = MemoryManager.get_all()

        self.assertEqual(
            result,
            expected
        )

    @patch.object(MemoryManager, "save")
    @patch.object(MemoryManager, "load")
    def test_update(self, mock_load, mock_save):

        mock_load.return_value = {
            "name": "Vagish"
        }

        facts = {
            "skills": [
                "Python"
            ]
        }

        MemoryManager.update(facts)

        mock_save.assert_called_once_with({
            "name": "Vagish",
            "skills": [
                "Python"
            ]
        })

    @patch("builtins.open")
    def test_load_failure_returns_empty_dict(self, mock_open):

        mock_open.side_effect = FileNotFoundError

        result = MemoryManager.load()

        self.assertEqual(
            result,
            {}
        )


if __name__ == "__main__":
    unittest.main()