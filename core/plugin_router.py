from core.plugin_loader import PluginLoader


class PluginRouter:

    def __init__(self):

        self.plugins = []

        for module in PluginLoader.load():

            for item in module.__dict__.values():

                if isinstance(item, type):

                    self.plugins.append(item)

    def execute(self, command):

        command = command.lower()

        for plugin in self.plugins:

            if hasattr(plugin, "keywords"):

                if any(
                    keyword in command
                    for keyword in plugin.keywords
                ):

                    return plugin.execute(command)

        return None