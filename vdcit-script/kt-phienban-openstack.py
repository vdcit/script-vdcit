################################################
## Chuong trinh kiem tra phien ban OpenStack
## VDC-IT
## Cách thực hiện
# python kt-phienban-openstack.py
## Ngày cập nhật: 18/08/2014
################################################

#!/bin/python

from nova import version
print "Phien ban OpenStack hien tai la: ", version.version_string()
