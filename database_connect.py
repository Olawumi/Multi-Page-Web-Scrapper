import mysql.connector
from sqlalchemy import create_engine

cntn = mysql.connector.connect(host = 'localhost', user = 'your_username', password = 'your_password', database = 'ng_trade')
cur = cntn.cursor()
engine = create_engine('mysql://"your_username":"your_password"@localhost/ng_trade')
cur.execute('SELECT * from trade_data')
print(engine.table_names())
