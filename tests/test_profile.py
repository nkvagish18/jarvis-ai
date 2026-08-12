import unittest
from unittest.mock import patch

from memory.profile import Profile


class TestProfile(unittest.TestCase):

    @patch("memory.profile.MemoryManager.update")
    def test_remember_facts(self, mock_update):

        facts = {
            "name": "Vagish",
            "skills": ["Python"]
        }

        Profile.remember(facts)

        mock_update.assert_called_once_with(facts)

    @patch("memory.profile.MemoryManager.update")
    def test_remember_empty_facts(self, mock_update):

        Profile.remember({})

        mock_update.assert_not_called()

    @patch("memory.profile.MemoryManager.update")
    def test_remember_none(self, mock_update):

        Profile.remember(None)

        mock_update.assert_not_called()

    @patch("memory.profile.MemoryManager.get_all")
    def test_get_profile(self, mock_get_all):

        expected = {
            "name": "Vagish",
            "skills": ["Python", "AI"]
        }

        mock_get_all.return_value = expected

        result = Profile.get()

        self.assertEqual(
            result,
            expected
        )

        mock_get_all.assert_called_once()


if __name__ == "__main__":
    unittest.main()