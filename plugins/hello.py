class HelloPlugin:

    keywords = [
        "hello jarvis",
        "hi jarvis"
    ]

    @staticmethod
    def execute(command):

        return (
            "Hello Vagish! How can I help you today?"
        )