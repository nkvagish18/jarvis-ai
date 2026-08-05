from datetime import datetime


class System:

    @staticmethod
    def get_time():
        try:
            return datetime.now().strftime("The time is %I:%M %p")

        except Exception as e:
            print(f"[System Error] {e}")
            return "I couldn't retrieve the current time."

    @staticmethod
    def get_date():
        try:
            return datetime.now().strftime("Today is %d %B %Y")

        except Exception as e:
            print(f"[System Error] {e}")
            return "I couldn't retrieve today's date."