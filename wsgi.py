from dotenv import load_dotenv
load_dotenv()

from app import app

if __name__ == "__main__":
    import gunicorn, psycopg2, pypugjs, pretty_errors
    app.run(debug=True)
