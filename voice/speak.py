import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        # Voice settings
        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)


    def speak(self, text):
        print("Jarvis:", text)

        self.engine.say(text)
        self.engine.runAndWait()


# Test
if __name__ == "__main__":
    jarvis = Speaker()
    jarvis.speak("Hello Vagish, I am Jarvis. My voice system is ready.")