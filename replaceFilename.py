import os
import sys

def rename_file( dir ):
    def rename_all( root, items ):
        for name in items:
            try:
                if " " in name: # REPLACE WITH SOURCE CHARACTERS
                    print ("Found: {0}".format(name))
                    os.rename(os.path.join(root, name), os.path.join(root, name.replace(' ', '-', 1))) # REPLACE WITH BOTH SOURCE AND DESIRED CHARACTERS
            except OSError as e:
                print ("OSError ({0}): {1} - {2}".format(e.errno, e.strerror, name))
    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all(root,dirs)
        rename_all(root,files)
        
if len(sys.argv) == 1: # Check for proper argument count
    print ("Error: Invalid Syntax")
    print ("Usage: replaceFilename.py C:\\DirToRename\\")
elif len(sys.argv) > 2: # Check for too many arguments
    print ("Error: Too Many Arguments")
    print ("Usage: replaceFilename.py C:\\DirToRename\\")
else:
    if os.path.isdir(sys.argv[1]): # Check for valid Path
        rename_file(sys.argv[1])
    else:
        print ("Error: Invalid Path")
        print ("Usage: replaceFilename.py C:\\DirToRename\\")