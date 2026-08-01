from datetime import datetime

class System:

    @staticmethod
    def get_time():
        return datetime.now().strftime("The time is %I:%M %p")

    @staticmethod
    def get_date():
        return datetime.now().strftime("Today is %d %B %Y")