from sqlalchemy.engine import create_engine


DIALECT = "oracle"
SQL_DRIVER = "cx_oracle"
USERNAME = "admin"
PASSWORD = "ZyKMPY4PAKnrZhf"
HOST = "adb.ap-mumbai-1.oraclecloud.com"
PORT = 1522
DB_NAME="Webapp"
#"dialect+driver://username:password@host:port/database”.
db_URL=f"{DIALECT}+{SQL_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

try:
    engine = create_engine(db_URL)
    print("Connection made succesfully")
except Exception as ex:
    print("Connection not made ERR:",ex)