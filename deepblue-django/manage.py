#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # set export GOOGLE_MAPS_API_KEY=AIzaSyDdULiINZ9XPR3hnDkQoOu-djYxWe3H7_Q
    os.environ.setdefault('GOOGLE_MAPS_API_KEY', 'AIzaSyDdULiINZ9XPR3hnDkQoOu-djYxWe3H7_Q')
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deepblue.settings')
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
