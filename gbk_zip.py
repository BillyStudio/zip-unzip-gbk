#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from zipfile import ZipFile 
from zipfile import ZipInfo
import os
import sys

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    # returning all file paths
    return file_paths

# path to folder which needs to be zipped
directory = sys.argv[1];

# calling function to get all file paths in the directory
file_paths = get_all_file_paths(directory)

# printing the list of all files to be zipped
print('Following files will be zipped:')
for file_name in file_paths:
    print(file_name)

# writing files to a zipfile
with ZipFile(sys.argv[2], 'w') as zip:
    # writing each file one by one
    for file_name in file_paths:
        fo = open(file_name, 'rb')
        print(file_name.decode('utf-8').encode('gbk'))
        gbkfileinfo = ZipInfo(file_name.decode('utf-8').encode('gbk'))
        zip.writestr(gbkfileinfo, fo.read())
        fo.close()

print('All files zipped successfully!')

