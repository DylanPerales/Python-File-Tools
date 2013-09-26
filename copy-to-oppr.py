import os
import sys
import shutil

# String Arrays for OPPR Servers
opprProd = ["cnndcdomp007.nndc.kp.org","cnndcdomp008.nndc.kp.org","cnndcdomp009.nndc.kp.org","cnndcdomp010.nndc.kp.org","cnndcdomp011.nndc.kp.org","cnndcdomp012.nndc.kp.org","masdcopap001.ssdc.kp.org","masdcopap002.ssdc.kp.org","masdcopap003.ssdc.kp.org","masdcopap004.ssdc.kp.org","masdcopap005.ssdc.kp.org","masdcopap006.ssdc.kp.org","masdcopap007.ssdc.kp.org","masdcopap008.ssdc.kp.org","masdcopap009.ssdc.kp.org","masdcopap010.ssdc.kp.org"]
opprFirst = ["cnndcdomp007.nndc.kp.org","cnndcdomp009.nndc.kp.org","cnndcdomp011.nndc.kp.org","masdcopap001.ssdc.kp.org","masdcopap003.ssdc.kp.org","masdcopap005.ssdc.kp.org","masdcopap007.ssdc.kp.org","masdcopap009.ssdc.kp.org"]
opprSecond = ["cnndcdomp008.nndc.kp.org","cnndcdomp010.nndc.kp.org","cnndcdomp012.nndc.kp.org","masdcopap002.ssdc.kp.org","masdcopap004.ssdc.kp.org","masdcopap006.ssdc.kp.org","masdcopap008.ssdc.kp.org","masdcopap010.ssdc.kp.org"]
opprDev = ["cnwdcopad001.wcdc.kp.org","cnwdcopad002.wcdc.kp.org","masdcopap011.ssdc.kp.org","masdcopap012.ssdc.kp.org"]
opprTest = ["cnwdcopad001.wcdc.kp.org"]

# Function to Copy a File
def copy_file( src, dest ):
    for server in opprDev:
        destPath = '\\\\' + server + '\\' + dest # Destination path on server
        try:
            shutil.copy(src, destPath)
            print ("Copied: {0} to {1}".format(src, destPath))
        except shutil.Error as e:
            print ("Error copying: ({0}): {1} - {2} to {3}".format(e.errno, e.strerror, src, destPath))
# Function to Copy a Folder
def copy_folder( src, dest ):
    for server in opprDev:
        destPath = '\\\\' + server + '\\' + dest # Destination path on server
        try:
            shutil.copytree(src, destPath)
            print ("Copied: {0} to {1}".format(src, destPath))
        except shutil.Error as e:
            print ("Error copying: ({0}): {1} - {2} to {3}".format(e.errno, e.strerror, src, destPath))
if len(sys.argv) == 1:
    print ("Error: Invalid Syntax")
    print ("Usage: copy-to-oppr.py file-or-folder-to-copy dest-path")
    print ("Usage: For Server Lists type copy-to-oppr.py help")
# elif sys.argv[1] == 'help':
    # print ("Usage: copy-to-oppr.py file-or-folder-to-copy dest-path servers")
    # print ("opprProd = ", opprProd)
    # print ("opprFirst = ", opprFirst)
    # print ("opprSecond = ", opprSecond)
    # print ("opprDev = ", opprDev)
    # print ("opprTest = ", opprTest)
elif os.path.exists(sys.argv[1]): # Check for valid Path
        if os.path.isfile(sys.argv[1]):
            copy_file(sys.argv[1], sys.argv[2])
        else:
            copy_folder(sys.argv[1], sys.argv[2])
else:
    print ("Error: Invalid Path")
    print ("Usage: copy-to-oppr.py file-or-folder-to-copy")