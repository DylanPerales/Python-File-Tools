import os
import sys
import shutil

# String Array for desired hosts to copy to
hostList = ["host1","host2","host3"]

# Function to Copy a File
def copy_file( src, dest ):
    for host in hostList:
        destPath = '\\\\' + host + '\\' + dest # Destination path on host
        try:
            shutil.copy(src, destPath)
            print ("Copied: {0} to {1}".format(src, destPath))
        except shutil.Error as e:
            print ("Error copying: ({0}): {1} - {2} to {3}".format(e.errno, e.strerror, src, destPath))
# Function to Copy a Folder
def copy_folder( src, dest ):
    for host in hostList:
        destPath = '\\\\' + host + '\\' + dest # Destination path on server
        try:
            shutil.copytree(src, destPath)
            print ("Copied: {0} to {1}".format(src, destPath))
        except shutil.Error as e:
            print ("Error copying: ({0}): {1} - {2} to {3}".format(e.errno, e.strerror, src, destPath))
if len(sys.argv) != 4:
    print ("Error: Invalid Arguments")
    print ("Usage: copy-to-host.py file-or-folder-to-copy dest-path")
elif os.path.exists(sys.argv[1]): # Check for valid Path
        if os.path.isfile(sys.argv[1]):
            copy_file(sys.argv[1], sys.argv[2])
        else:
            copy_folder(sys.argv[1], sys.argv[2])
else:
    print ("Error: Invalid Path")
    print ("Usage: copy-to-host.py file-or-folder-to-copy dest-path")
