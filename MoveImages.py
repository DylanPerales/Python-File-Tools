import os
import sys
import shutil

hostList = ["cnndcdomp007.nndc.kp.org","cnndcdomp008.nndc.kp.org","cnndcdomp009.nndc.kp.org","cnndcdomp010.nndc.kp.org","cnndcdomp011.nndc.kp.org","cnndcdomp012.nndc.kp.org","masdcopap001.ssdc.kp.org","masdcopap002.ssdc.kp.org","masdcopap003.ssdc.kp.org","masdcopap004.ssdc.kp.org","masdcopap005.ssdc.kp.org","masdcopap006.ssdc.kp.org","masdcopap007.ssdc.kp.org","masdcopap008.ssdc.kp.org","masdcopap009.ssdc.kp.org","masdcopap010.ssdc.kp.org"]

def copy_file( file ):
    for host in hostList:
        try:
            shutil.move(os.path.join(root, filename), dest)
                print ("Copied: {0}".format(filename))
                except shutil.Error as e:
                    print ("Error copying file: ({0}): {1} - {2}".format(e.errno, e.strerror, filename))
                    
if len(sys.argv) == 1:
    print ("Error: Invalid Syntax")
    print ("Usage: copy-file.py file-to-copy.ext")
elif len(sys.argv) > 2: # Check for too many arguments
    print ("Error: Too Many Arguments")
    print ("Usage: copy-file.py file-to-copy.ext")
else:
    if os.path.exists(sys.argv[1]): # Check for valid Path
        copy_file(sys.argv[1])
    else:
        print ("Error: Invalid Filename")
        print ("Usage: copy-file.py file-to-copy.ext"")