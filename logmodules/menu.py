from os import strerror
import pymysql

def select_query(con, sql):
    try:
         with con.cursor() as cur:
            cur.execute(sql)
            con.commit()
            for rows in cur:
                for row in rows:
                    print(rows[row], end="\t")
                print("")
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False
    finally:
        con.close()
