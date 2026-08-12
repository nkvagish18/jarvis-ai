import unittest

from memory.conversation import ConversationMemory


class TestConversationMemory(unittest.TestCase):

    def test_empty_context(self):

        memory = ConversationMemory()

        self.assertEqual(
            memory.get_context(),
            ""
        )

    def test_add_user_message(self):

        memory = ConversationMemory()

        memory.add_user("Hello Jarvis")

        self.assertEqual(
            memory.get_context(),
            "User: Hello Jarvis"
        )

    def test_add_assistant_message(self):

        memory = ConversationMemory()

        memory.add_assistant("Hello Vagish!")

        self.assertEqual(
            memory.get_context(),
            "Assistant: Hello Vagish!"
        )

    def test_conversation_order(self):

        memory = ConversationMemory()

        memory.add_user("Hello")

        memory.add_assistant("Hi!")

        memory.add_user("How are you?")

        expected = (
            "User: Hello\n"
            "Assistant: Hi!\n"
            "User: How are you?"
        )

        self.assertEqual(
            memory.get_context(),
            expected
        )

    def test_max_messages(self):

        memory = ConversationMemory(max_messages=3)

        memory.add_user("Message 1")
        memory.add_assistant("Message 2")
        memory.add_user("Message 3")
        memory.add_assistant("Message 4")

        context = memory.get_context()

        self.assertNotIn(
            "Message 1",
            context
        )

        self.assertIn(
            "Message 2",
            context
        )

        self.assertIn(
            "Message 3",
            context
        )

        self.assertIn(
            "Message 4",
            context
        )

    def test_clear(self):

        memory = ConversationMemory()

        memory.add_user("Hello")

        memory.clear()

        self.assertEqual(
            memory.get_context(),
            ""
        )


if __name__ == "__main__":
    unittest.main()