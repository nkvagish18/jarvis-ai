from datetime import datetime

class Logger:

    @staticmethod
    def error(module, error):
        print(
            f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
            f"[{module}] ERROR: {error}"
        )

    @staticmethod
    def info(module, message):
        print(
            f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
            f"[{module}] INFO: {message}"
        )