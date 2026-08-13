import unittest
from unittest.mock import patch, MagicMock

from services.system_monitor import SystemMonitor


class TestSystemMonitor(unittest.TestCase):

    # ---------------- Battery ----------------

    @patch("services.system_monitor.psutil.sensors_battery")
    def test_battery_available(self, mock_battery):

        battery = MagicMock()
        battery.percent = 75
        battery.power_plugged = True

        mock_battery.return_value = battery

        result = SystemMonitor.battery()

        self.assertEqual(
            result,
            "Battery is 75 percent and it is currently charging."
        )

    @patch("services.system_monitor.psutil.sensors_battery")
    def test_battery_not_charging(self, mock_battery):

        battery = MagicMock()
        battery.percent = 40
        battery.power_plugged = False

        mock_battery.return_value = battery

        result = SystemMonitor.battery()

        self.assertEqual(
            result,
            "Battery is 40 percent and it is currently not charging."
        )

    @patch("services.system_monitor.psutil.sensors_battery")
    def test_battery_unavailable(self, mock_battery):

        mock_battery.return_value = None

        result = SystemMonitor.battery()

        self.assertEqual(
            result,
            "Battery information is not available."
        )

    # ---------------- CPU ----------------

    @patch("services.system_monitor.psutil.cpu_percent")
    def test_cpu(self, mock_cpu):

        mock_cpu.return_value = 35.5

        result = SystemMonitor.cpu()

        self.assertEqual(
            result,
            "CPU usage is 35.5 percent."
        )

        mock_cpu.assert_called_once_with(interval=1)

    # ---------------- Memory ----------------

    @patch("services.system_monitor.psutil.virtual_memory")
    def test_memory(self, mock_memory):

        memory = MagicMock()
        memory.percent = 60
        memory.available = 8 * (1024 ** 3)

        mock_memory.return_value = memory

        result = SystemMonitor.memory()

        self.assertEqual(
            result,
            "RAM usage is 60 percent. 8 GB available."
        )

    # ---------------- Disk ----------------

    @patch("services.system_monitor.psutil.disk_usage")
    def test_disk(self, mock_disk):

        disk = MagicMock()
        disk.percent = 50
        disk.free = 100 * (1024 ** 3)
        disk.total = 200 * (1024 ** 3)

        mock_disk.return_value = disk

        result = SystemMonitor.disk()

        self.assertEqual(
            result,
            "Disk usage is 50 percent. 100 GB free out of 200 GB."
        )

        mock_disk.assert_called_once_with("/")

    # ---------------- IP ----------------

    @patch("services.system_monitor.socket.socket")
    def test_ip(self, mock_socket):

        mock_connection = MagicMock()

        mock_connection.getsockname.return_value = (
            "192.168.1.10",
            12345
        )

        mock_socket.return_value = mock_connection

        result = SystemMonitor.ip()

        self.assertEqual(
            result,
            "Your IP address is 192.168.1.10."
        )

        mock_connection.connect.assert_called_once_with(
            ("8.8.8.8", 80)
        )

        mock_connection.close.assert_called_once()

    @patch("services.system_monitor.socket.socket")
    def test_ip_failure(self, mock_socket):

        mock_socket.side_effect = Exception(
            "Network unavailable"
        )

        result = SystemMonitor.ip()

        self.assertEqual(
            result,
            "Unable to determine your IP address."
        )


if __name__ == "__main__":
    unittest.main()