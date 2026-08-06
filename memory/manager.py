import json
import os
from utils.config import Config

class MemoryManager:

    FILE = Config.MEMORY_FILE

    @staticmethod
    def load():

        try:
            with open(
                MemoryManager.FILE,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except Exception:
            return {}

    @staticmethod
    def save(memory):

        with open(
            MemoryManager.FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                memory,
                f,
                indent=4,
                ensure_ascii=False
            )

    # ---------------- Deep Merge ----------------

    @staticmethod
    def deep_merge(old, new):

        for key, value in new.items():

            if (
                key in old
                and isinstance(old[key], dict)
                and isinstance(value, dict)
            ):

                MemoryManager.deep_merge(
                    old[key],
                    value
                )

            else:

                old[key] = value

        return old

    # ---------------- Update ----------------

    @staticmethod
    def update(facts):

        memory = MemoryManager.load()

        memory = MemoryManager.deep_merge(
            memory,
            facts
        )

        MemoryManager.save(memory)

    @staticmethod
    def get_all():

        return MemoryManager.load()