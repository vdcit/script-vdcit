#!usr/bin/python

import platform
import os

if platform.system() == 'Linux':

    a = platform.linux_distribution()
    b = os.uname()
    print 'You are using Linux !'
    print 'Your OS : %s' % a[0]
    print 'Os version : %s' % a[1]
    print 'Os version name : %s' % a[2]
    print 'HostName : %s ' % b[1]
    print 'Kernel : %s' % b[2]
    print 'Architecture : %s' % b[4]

if platform.system() == 'Windows':
    print 'You are using Windows'
    print 'Windows Version : %s' % platform.release()

if platform.system() == 'Darwin':
    print 'You are using Mac OS Rich !'
    print 'Mac version %s' % platform.mac_ver()


