from sqlalchemy.engine import URL
from .env import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DB, PG_SCHEMA

url_postgres = URL.create(
  drivername="postgresql+psycopg2",
  username=PG_USER,
  password=PG_PASSWORD,
  host=PG_HOST,
  port=PG_PORT,
  database=PG_DB
) 
