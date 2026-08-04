import subprocess


class Apps:

    @staticmethod
    def open_notepad():
        subprocess.Popen("notepad")
        return "Opening Notepad"

    @staticmethod
    def open_calculator():
        subprocess.Popen("calc")
        return "Opening Calculator"

    @staticmethod
    def open_cmd():
        subprocess.Popen("cmd")
        return "Opening Command Prompt"

    @staticmethod
    def open_paint():
        subprocess.Popen("mspaint")
        return "Opening Paint"

    @staticmethod
    def open_explorer():
        subprocess.Popen("explorer")
        return "Opening File Explorer"

    @staticmethod
    def open_notepad():
        try:
            subprocess.Popen("notepad")
            return "Opening Notepad."

        except Exception as e:
            print(f"[Apps Error] {e}")
            return "I couldn't open Notepad."