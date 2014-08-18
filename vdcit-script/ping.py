import os
import signal
import time
import subprocess
import sys
import datetime

"""Thay doi cau lenh va duong dan o day"""

host = raw_input('nhap vao ten host: ')
packets = int(raw_input('nhap vao so goi tin: '))
Command = 'ping google.com.vn'
directory = '/home/cherry/Documents'

p = subprocess.Popen('ping -c %d -q %s' %(packets, host), stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

p_status = p.wait()
output = output.split(',')
packets_r = int(output[1].strip('received'))
packets_l = packets-(int(packets_r))
packets_p = (float(packets_l)/float(packets))


a = output[3].split('\n')
b = a[1].split('/')
c = b[3]
d = c.split('=')

ms_min = d[1]
ms_max = b[5]



#print output
print "so goi tin da gui : ", packets
print "so goi tin da nhan lai: ", packets_r
print "so goi tin mat: ", packets_l
print "phan tram goi tin bi mat: ", "{:.2%}".format(packets_p)
print 'Thoi gian tra ve goi tin nhanh nhat %s ms' % ms_min
print 'Thoi gian tra ve goi tin cham nhat %s ms' % ms_max



