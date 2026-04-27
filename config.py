import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN: str = os.environ["DISCORD_TOKEN"]
DB_HOST: str = os.environ["DB_HOST"]
DB_USER: str = os.environ["DB_USER"]
DB_PASS: str = os.environ["DB_PASS"]
DB_NAME: str = os.environ["DB_NAME"]
