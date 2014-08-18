################################################
## Chuong trinh kiem tra phien ban OpenStack
## VDC-IT
## Ngay cap nhat: 18/08/2014
###############################################
## Cach thu hien
# python kt-phienban-openstack.py
################################################

#!/bin/python


from nova import version
print "Phien ban OpenStack hien tai la: ", version.version_string()
