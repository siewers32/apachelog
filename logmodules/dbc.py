import pymysql

def conn():
    return pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          database='apachelog',
                          port=3306,
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)