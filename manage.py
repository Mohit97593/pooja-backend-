#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nxtbn.settings')
    try:
        from django.core.management import execute_from_command_line
        import django.urls
        from django.urls import converters
        original_register_converter = converters.register_converter
        def register_converter(converter, type_name):
            try:
                original_register_converter(converter, type_name)
            except ValueError as e:
                if f"Converter {type_name!r} is already registered." in str(e):
                    pass
                else:
                    raise
        converters.register_converter = register_converter
        django.urls.register_converter = register_converter
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
