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

Used to modify multiple files filenames, replacing strings within filename (e.x. '-' to '_').
#### Usage:
`FilenameReplacer.py`

The program will then ask for the Directory to search, string to replace and what to replace it with
Example: 

>Enter directory of contents you wish to rename: E:\Test\n
>Enter name or string to replace: - <br />
>Enter desired name or string: _ <br />
>Renamed: file-1.txt to file_1.txt <br />
>Renamed: file-2.txt to file_2.txt <br />
>Renamed: file-3.txt to file_3.txt

##### Before:
  * \test\file-1.txt 
  * \test\file-2.txt 
  * \test\file-3.txt 

##### After:
  * \test\file_1.txt 
  * \test\file_2.txt 
  * \test\file_3.txt 
