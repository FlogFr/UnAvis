#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":

    DEBUG = os.getenv('DEBUG', False)
    TEST = os.getenv('TEST', False)

    if DEBUG:
        os.environ.setdefault("DJANGO_CONFIGURATION",
                              "DevelopmentConfiguration")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "UnAvis.settings.development")
    elif TEST:
        os.environ.setdefault("DJANGO_CONFIGURATION",
                              "DefaultConfiguration")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "UnAvis.settings.defaults")
    else:
        os.environ.setdefault("DJANGO_CONFIGURATION",
                              "ProductionConfiguration")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "UnAvis.settings.production")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
