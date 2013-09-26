import os
import sys
# Removes capitalization recursively in a directory
def lowercase_rename( dir ):
    def rename_all( root, items ):
        for name in items:
            try:
                os.rename(os.path.join(root, name),os.path.join(root, name.lower()))
            except OSError:
                print ("Unable to rename: " + name)
# Starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all(root,dirs)
        rename_all(root,files)

if len(sys.argv) == 1:
    print ("Error: Invalid Syntax")
    print ("Usage: dirRenameLower.py \\DirToRename\\")
elif len(sys.argv) > 2:
    print ("Error: Too Many Arguments")
    print ("Usage: dirRenameLower.py \\DirToRename\\")
else:
    if os.path.isdir(sys.argv[1]):
        lowercase_rename(sys.argv[1])
    else:
        print ("Error: Invalid Path")
        print ("Usage: dirRenameLower.py \\DirToRename\\")