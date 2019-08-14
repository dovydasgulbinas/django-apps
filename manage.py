#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # TODO: ADD automatic selection
    # dsm = os.environ.get('DJANGO_SETTINGS_MODULE')
    # print(dsm)
    # print(not dsm)
    # print(dsm in ('None', 'none', 'False', 'false', '\'\'', '""'))
    # if (not dsm) or (dsm in ('None', 'none', 'False', 'false', '\'\'', '""')):
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showcase.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showcase.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()