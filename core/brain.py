from core.router import Router


class Brain:

    def __init__(self):
        self.router = Router()

    def process(self, command):
        return self.router.route(command)