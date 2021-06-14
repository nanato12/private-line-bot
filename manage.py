import os
import sys

from core import exec_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("COMMAND_OUTPUT_PATH", "commands")
    os.environ.setdefault("EVENT_OUTPUT_PATH", "events")
    os.environ.setdefault("ENV_OUTPUT_PATH", "settings")
    exec_from_command_line(sys.argv)
