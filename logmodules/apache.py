from os import strerror
import pymysql
from apachelogs import LogParser
import datetime

def parser():
    return LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# def conn():
#     return pymysql.connect(host='localhost',
#                           user='root',
#                           password='',
#                           database='apachelog',
#                           port=3306,
#                           charset='utf8mb4',
#                           cursorclass=pymysql.cursors.DictCursor)

def parseLog(parser):
    entries = []
    with open('small_apache.log') as fp:  # doctest: +SKIP
        for entry in parser.parse_lines(fp,  ignore_invalid=True):
            query = str(entry.request_line).split()
            x = entry.request_time
            if entry.bytes_sent != None:
                bytes_sent = entry.bytes_sent
            else:
                bytes_sent = 0

            items = {"time": x.strftime("%Y-%m-%d %H:%M:%S"),
                    "len": bytes_sent,
                    "useragent": entry.headers_in['User-Agent'],
                    "referer": entry.headers_in['Referer'],
                    "method": query[0].strip("/"),
                    "log": "",
                    "ip": entry.directives["%h"]}

            try:
                items["page"] = query[1]
            except IndexError:
                items["page"] = "Non page"
            try:
                items["protocol"] = query[2]
            except IndexError:
                items["protocol"] = "No protocol"

            entries.append(items)
    return entries


def cleardb(con):
    try:
        with con.cursor() as cur:
            sql = "DELETE FROM apache_log"
            cur.execute(sql)
            con.commit()
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False
    except:
        print("Log tabel leemaken is mislukt!")

def savetodb(con, entries):
    try:
        for items in entries:
            with con.cursor() as cur:
                sql = "INSERT INTO `apache_log` (`time`, `len`,`useragent`, `page`, `method`, `protocol`, `log`, `ip`) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                # sql = "INSERT INTO `log` (`time`) VALUES (%s)"
                # cur.execute(sql, (items['time']))
                cur.execute(sql, (
                   items['time'],
                   int(items['len']),
                   items['useragent'],
                   items['page'],
                   items['method'],
                   items['protocol'],
                   items['log'],
                   items['ip']
                ))
                con.commit()

    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False
    except:
        print("records toevoegen is mislukt")
    finally:
        print("Apache log is overgezet naar MySQL")
        con.close()

# logentries = parseLog(parser)
# savetodb(conn(), logentries)