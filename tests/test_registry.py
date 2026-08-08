import unittest

from core.command_registry import CommandRegistry


class TestCommandRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = CommandRegistry()

        self.registry.register(
            ["hello", "hi"],
            lambda command: "Hello!"
        )

    def test_registered_command(self):

        result = self.registry.execute(
            "hello jarvis"
        )

        self.assertEqual(
            result,
            "Hello!"
        )

    def test_unknown_command(self):

        result = self.registry.execute(
            "calculate 12345"
        )

        self.assertIsNone(result)

    def test_partial_keyword_should_not_match(self):

        result = self.registry.execute(
            "spaceship"
        )

        self.assertIsNone(result)


    def test_keyword_inside_word_should_not_match(self):

        result = self.registry.execute(
            "display something"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()