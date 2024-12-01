#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Handle PyInstaller environment
    if getattr(sys, 'frozen', False):
        # If running as a PyInstaller bundled app
        os.environ['DJANGO_SETTINGS_MODULE'] = 'soul.settings'
        os.environ['PYTHONHOME'] = sys._MEIPASS  # PyInstaller's temp directory
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soul.settings')

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
