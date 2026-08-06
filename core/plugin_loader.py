import importlib
import pkgutil

import plugins


class PluginLoader:

    @staticmethod
    def load():

        loaded = []

        for _, module_name, _ in pkgutil.iter_modules(
            plugins.__path__
        ):

            module = importlib.import_module(
                f"plugins.{module_name}"
            )

            loaded.append(module)

        return loaded
    