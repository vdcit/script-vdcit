################################################
## Chuong trinh kiem tra phien ban OpenStack
## VDC-IT
## Ngày cập nhật: 18/08/2014
###############################################
## Cách thực hiện
# python kt-phienban-openstack.py
################################################

#!/bin/python

from nova import version
print "Phien ban OpenStack hien tai la: ", version.version_string()
