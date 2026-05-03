from django.db import connection
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    print("Extension pg_trgm enabled successfully.")
except Exception as e:
    print(f"Error enabling extension: {e}")
