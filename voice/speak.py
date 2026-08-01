import asyncio
import edge_tts
import pygame
import tempfile
import os


class Speaker:

    def __init__(self):
        pygame.mixer.init()

        # Change this voice later if you like
        self.voice = "en-US-AriaNeural"

    async def _generate(self, text, filename):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(filename)

    def speak(self, text):

        print("Jarvis:", text)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name

        asyncio.run(self._generate(str(text), filename))

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        os.remove(filename)


if __name__ == "__main__":
    speaker = Speaker()

    speaker.speak("Hello Vagish.")
    speaker.speak("This is Jarvis.")
    speaker.speak("Everything is working perfectly.")