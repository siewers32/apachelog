from apachelogs import LogParser
from os import strerror
import pymysql

# Connect to the database
con = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='apachelog',
                      port=3306,
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

try:
    for line in open('small_access.log', 'rt'):
        entry = parser.parse(line)
        s = str.split(entry.directives["%r"])
        with con.cursor() as cur:
            sql = "INSERT INTO `log` (`method`, `page`,`protocol`) VALUES (%s, %s, %s)"
            cur.execute(sql, (s[0], s[1], s[2]))
            con.commit()



except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
finally:
    con.close()