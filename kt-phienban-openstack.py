################################################
## Chuong trinh kiem tra phien ban OpenStack
## VDC-IT
################################################

#!/bin/python

from nova import version
print "Phien ban OpenStack hien tai la: "version.version_string()
