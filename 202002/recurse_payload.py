

import os

path = input("Enter payload path: ")

if not os.path.exists(path):
    print('Path must be exist! ', path)
    pass
   
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    #print(os.path.basename(root))
    for name in files:
        print(os.path.join(root, name))
        
