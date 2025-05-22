import os
from os import path
import shutil
from zipfile import ZipFile

# making a copy of an existing file
if path.exists("newfile.txt"):

    # Get path to the file in the current directory
    source = path.realpath("newfile.txt")

    # making a back up copy
    # destination = source + ".bak"
    # shutil.copy(source, destination)

    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    # put things into a ZIP archive
    # root_dir, tail = path.split(source)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine grain control over zip file
    # local scope once everything goes out of scope the zipfile will automatically be closed
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")
