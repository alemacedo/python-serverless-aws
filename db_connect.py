import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'numen_rh',
  'raise_on_warnings': True
}

db_con = mysql.connector.connect(**config)

def runQuery(sql, filterName):
  
  if filterName:
    sql = sql + " where name_full like '%{}%'".format(filterName)

  cursor = db_con.cursor()
  cursor.execute(sql)
  return cursor.fetchall()




