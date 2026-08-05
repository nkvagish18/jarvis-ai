from memory.manager import MemoryManager


class Profile:

    @staticmethod
    def remember(facts):

        if facts:
            MemoryManager.update(facts)

    @staticmethod
    def get():

        return MemoryManager.get_all()