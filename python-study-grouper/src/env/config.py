from os import path, getenv
from dotenv import load_dotenv

# Path to the database directory
directory = path.dirname(__file__)

try:
    load_dotenv(dotenv_path=path.join(directory, "..", ".env"))
except FileNotFoundError:
    # this doesnt seem to ever give error no matter what.. ?
    print(".env file not found")

DATABASE_NAME = getenv("DATABASE") or "db.sqlite3"
DATABASE_PATH = path.join(directory, "Data", DATABASE_NAME)
