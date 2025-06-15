from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote

# Carregar variaveis de ambiente
load_dotenv()

# Project Paths
BASE_DIR = Path(__file__).parent.resolve()
PROJECT_DIR = BASE_DIR.parent


# Database
DATABASE_DIR = PROJECT_DIR / "data"
DATABASE_NAME = 'process_mining.db'
SQLITE_DATABASE_URL = 'sqlite:///{}'.format(quote((DATABASE_DIR / DATABASE_NAME).as_posix(), safe=":/\\"))
