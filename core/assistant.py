from core.ai import AI
from voice.listen import Listener
from voice.speak import Speaker
from core.brain import Brain
from utils.logger import logger


class Assistant:

    def __init__(self):

        self.ai = AI()
        self.listener = Listener()
        self.speaker = Speaker()
        self.brain = Brain()


    def start(self):

        self.speaker.speak(
            "Hello Vagish, Jarvis is online."
        )


        while True:

            command = self.listener.listen()

            logger.info("You: %s", command)

            response = self.brain.process(command)

            if response == "shutdown":
                self.speaker.speak("Goodbye Vagish")
                break

            if response is None:
                response = self.ai.ask(command)

            # Handle news headlines
            if isinstance(response, list):

                self.speaker.speak("Here are today's top headlines.")

                words = ["First", "Second", "Finally"]

                for i, headline in enumerate(response):
                    self.speaker.speak(words[i])
                    self.speaker.speak(headline)

            else:
                self.speaker.speak(response)