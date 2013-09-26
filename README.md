PythonFileTools
===============

Misc. Python tools used for file operations (Copy, Rename, etc.)
Originally geared towards work stuff, modifying for personal use.
All scripts used are intended for recursive use.


### Copy-to-hosts.py

Used to copy a file or folder (recursively), to multiple hosts.
Modify the **hostList** string array to the desired host list.
This will possibly be modified to a host list.
#### Usage:
`copy-to-host.py \file-or-folder-to-copy \dest-path`


### Decapitalizer.py

Used to remove any capitalization (again recursively) within a folder.
#### Usage:
`Decapitalizer.py \DirToRename\`


### FilenameReplacer.py

Used to modify multiple files filenames, replacing chars within filename (e.x. '-' to '_').
#### Usage:
`FilenameReplacer.py \DirToRename\ srcChar destChar`

Example: `FilenameReplacer.py \txtfiles\ - _`
##### Before:
  * \txtfiles\file-1.txt 
  * \txtfiles\file-2.txt 
  * \txtfiles\file-3.txt 

##### After:
  * \txtfiles\file_1.txt 
  * \txtfiles\file_2.txt 
  * \txtfiles\file_3.txt 
