# -*- coding: utf-8 -*-
import csv
import requests
import hashlib
from bs4 import BeautifulSoup
import hashlib
import sys
import os
import subprocess

def python_call_powershelladd():
    try:
        args=[r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe","-ExecutionPolicy","Unrestricted", r"C:\20170316-script-ACLManagement\ManageACLadd.ps1"]
        # args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception, e:
        print e
    return False

def python_call_powershelldel():
    try:
        args=[r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe","-ExecutionPolicy","Unrestricted", r"C:\20170316-script-ACLManagement\ManageACLdel.ps1"]
        # args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception, e:
        print e

def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,"html.parser").iframe
    return soup["src"]

def md5sum(fname):
    """ 计算文件的MD5值 """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(fname, basestring) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()
startmd5 = md5sum('C:\\20170316-script-ACLManagement\\addACL.csv')
print 'startmd5',startmd5
aip = get_out_ip(get_real_url())


csvfile = file('C:\\20170316-script-ACLManagement\\addACL.csv','rb')

readercon = csv.reader(csvfile)
alist = [['ServiceName', 'VMName', 'EndpointName', 'Order', 'Action', 'RemoteSubnet', 'Description']]
next(readercon)
for line in readercon:
    if line[5] != aip + '/32':
        line[5] = aip + '/32'
        alist.append(line)
    else:
        alist.append(line)
csvfile.close()
#print alist
csvfile1 = file('C:\\20170316-script-ACLManagement\\addACL.csv', 'wb')
writecon = csv.writer(csvfile1)
writecon.writerows(alist)
csvfile1.close()

endmd5 = md5sum('C:\\20170316-script-ACLManagement\\addACL.csv')
print 'endmd5',endmd5
if startmd5 != endmd5:
    print "start change ip"
    python_call_powershelldel()
    python_call_powershelladd()



