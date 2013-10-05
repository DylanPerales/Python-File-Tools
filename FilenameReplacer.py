import os
import sys

# Main function takes directory, original and desired characters to replace
def rename_file( dir, src, dest ):
    def rename_all( root, items ):
        for name in items:
            try:
                if src in name: # REPLACE WITH SOURCE CHARACTERS
                    print ("Found: {0}".format(name))
                    os.rename(os.path.join(root, name), os.path.join(root, name.replace(src, dest, 1))) # REPLACE WITH BOTH SOURCE AND DESIRED CHARACTERS
            except OSError as e:
                print ("OSError ({0}): {1} - {2}".format(e.errno, e.strerror, name))
    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all(root,dirs)
        rename_all(root,files)
        
# Validate proper number of arguments
if len(sys.argv) != 4:
    print ("Error: Invalid Arguments")
    print ("Usage: FilenameReplacer.py \\DirToRename\\ srcChar destChar")
else:
    if os.path.isdir(sys.argv[1]): # Check for valid Path
        rename_file(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print ("Error: Invalid Path")
        print ("Usage: FilenameReplacer.py \\DirToRename\\ srcChar destChar")