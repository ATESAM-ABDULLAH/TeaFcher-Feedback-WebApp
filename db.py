import oracledb

username="admin"
password="ZyKMPY4PAKnrZhf"
dsn="webapp_high"
dir="/home/atesam/Documents/Projects/Flask-WebApp/database/Wallet_Webapp"

con = oracledb.connect(
    user=username,
    password=password,
    dsn=dsn,
    config_dir=dir,
    wallet_location=dir,
    wallet_password=password
    )

print("Database connected")

cur=con.cursor()


con.commit()