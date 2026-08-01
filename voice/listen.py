import speech_recognition as sr


class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()


    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            # Reduce background noise
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = self.recognizer.listen(source)


        try:

            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            return text.lower()


        except sr.UnknownValueError:

            return "I didn't understand"


        except sr.RequestError:

            return "Internet error"



if __name__ == "__main__":

    jarvis = Listener()

    command = jarvis.listen()

    print("You:", command)