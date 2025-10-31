"""
Entry point for @vercel/python.  (It has to be placed
at the top level so that it can find pyproject.toml.)
"""

from clubradar.wsgi import app
