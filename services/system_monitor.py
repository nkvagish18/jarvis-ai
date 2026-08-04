import psutil
import socket


class SystemMonitor:

    @staticmethod
    def battery():

        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is not available."

        charging = "charging" if battery.power_plugged else "not charging"

        return (
            f"Battery is {battery.percent:.0f} percent "
            f"and it is currently {charging}."
        )

    @staticmethod
    def cpu():

        usage = psutil.cpu_percent(interval=1)

        return f"CPU usage is {usage} percent."

    @staticmethod
    def memory():

        memory = psutil.virtual_memory()

        return (
            f"RAM usage is {memory.percent} percent. "
            f"{memory.available // (1024 ** 3)} GB available."
        )

    @staticmethod
    def disk():

        disk = psutil.disk_usage("/")

        free = disk.free // (1024 ** 3)
        total = disk.total // (1024 ** 3)

        return (
            f"Disk usage is {disk.percent} percent. "
            f"{free} GB free out of {total} GB."
        )

    @staticmethod
    def ip():

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()

            return f"Your IP address is {ip}."

        except Exception:
            return "Unable to determine your IP address."