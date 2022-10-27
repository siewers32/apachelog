from os import strerror
from openstack import parse
from openstack import savetodb as openstack_save
from logmodules import apache
from logmodules import menu

# parsed = parse('openstack.log')

# openstack_save(parse('openstack.log'))

con = apache.conn()
# parser = apache.parser()
# apache.savetodb(con, apache.parseLog(parser))

query1 = "select useragent, count(useragent) as aantal from apache_log group by useragent order by aantal desc";
menu.query(con, query1)

