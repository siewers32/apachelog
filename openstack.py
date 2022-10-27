from os import strerror
import pymysql

def parse(file):
    try:
        lines = []
        for line in open(file, 'rt'):
            log = line.split()[0]
            if log[:8] == 'nova-api':
                ip = line.split("]")[1].split()[0]
                if ip[:2].isnumeric():
                    time = line.split("time:")[1][:-1]
                    len = line.split("len:")[1].split()[0]
                    status = line.split("status:")[1].split()[0]
                    page = line.split("\"")[1].split()[1]
                    method = line.split("\"")[1].split()[0]
                    protocol = line.split("\"")[1].split()[2]
                else:
                    time = len = status = page = method = protocol = "0"
                lines.append({'time': time, 'ip': ip, 'len': len, 'status': status, 'page': page, 'method': method,
                              'protocol': protocol, 'log': log})
        return lines
    except IndexError as e:
        print("IndexError occurred: ", e.args)
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))


def savetodb(lines):
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='root',
                          database='apachelog',
                          port=8889,
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    try:
        for l in lines:
            with con.cursor() as cur:
                sql = "INSERT INTO `openstack_log` (`time`, `len`,`status`, `page`, `method`, `protocol`, `log`, `ip`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (float(l['time']), int(l['len']), l['status'], l['page'], l['method'], l['protocol'], l['log'], l['ip']))
                con.commit()
    finally:
        con.close()