import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,text

load_dotenv()
url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
engine = create_engine(url)


con = engine.connect()
res = con.execute(text("select * from product"))
print(res.all())