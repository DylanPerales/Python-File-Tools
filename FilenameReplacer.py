import os
import sys
validDir = 0
found = False

def rename_file( dir, src, dest ):
	def rename_all( root, items ):
		for name in items:
			try:
				if src in name: # REPLACE WITH SOURCE CHARACTERS
					global found
					found = True
					newName = name.replace(src, dest, 1)
					os.rename(os.path.join(root, name), os.path.join(root, name.replace(src, dest, 1))) # REPLACE WITH BOTH SOURCE AND DESIRED CHARACTERS
					print ("Renamed: {0} to {1}".format(name, newName))
			except OSError as e:
				print ("OSError ({0}): {1} - {2}".format(e.errno, e.strerror, name))
	# starts from the bottom so paths further up remain valid after renaming
	for root, dirs, files in os.walk( dir, topdown=False ):
		rename_all(root,dirs)
		rename_all(root,files)
		
# Existing argument based checks
#if len(sys.argv) != 4: # Check for too many arguments
#    print ("Error: Invalid Arguments")
#    print ("Usage: FilenameReplacer.py \\DirToRename\\ srcChar destChar")


while (validDir == 0):
	if (sys.version_info.major < 3):
		renamePath = raw_input("Enter directory of contents you wish to rename: ")
	else:
		renamePath = input("Enter directory of contents you wish to rename: ")
	if (len(renamePath) == 0):
		exit(0)
	elif os.path.isdir(renamePath): # Check for valid Path
		validDir = 1
		if (sys.version_info.major < 3):
			origName = raw_input("Enter name or string to replace: ")
			newName = raw_input("Enter desired name or string: ")
		else:
			origName = input("Enter name or string to replace: ")
			newName = input("Enter desired name or string: ")
		rename_file(renamePath, origName, newName)
		if (found == False):
			print ("Nothing found matching: " + origName)
	else:
		print ("Error: Invalid Path")
		print ("Example: C:\\DirToRename\\ or //home//user//folder//")