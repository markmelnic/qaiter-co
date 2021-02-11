try:
    import envars
except ImportError:
    pass

import os

from app import app

if __name__ == "__main__":
    import gunicorn, psycopg2, pypugjs, pretty_errors, png
    app.run(debug=True)
