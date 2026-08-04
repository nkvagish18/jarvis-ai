from datetime import datetime

class System:

    try:

        @staticmethod
        def get_time():
            return datetime.now().strftime("The time is %I:%M %p")

        @staticmethod
        def get_date():
            return datetime.now().strftime("Today is %d %B %Y")

    except Exception as e:
        print(f"[System Error] {e}")
        return (
            "I couldn't retrieve your system information right now."
        )