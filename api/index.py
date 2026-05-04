try:
    import setuptools
except ImportError:
    pass

from nxtbn.wsgi import application

# This is the entry point for Vercel - Version 2
app = application
