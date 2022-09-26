from os import strerror
from openstack import parse
from openstack import savetodb

parsed = parse('openstack.log')
print(parsed)
save = savetodb(parsed)

