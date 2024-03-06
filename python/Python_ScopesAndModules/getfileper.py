import os
import stat
import sys
# exercise5:


def find_files(filename):
    for root, dirs, files in os.walk("/"):
        if filename in files:
            return os.path.join(root, filename)
    return None


def find_and_perm(file):
    file_path = find_files(file)
    if file_path:
        if not os.access(file, os.X_OK):
            os.chmod(file_path, os.stat(file_path).st_mode | stat.S_IXGRP | stat.S_IXUSR)
            print("File Permissions changed!")
        else:
            print("File has permissions!")
    else:
        print("File Not Found!")


find_and_perm(sys.argv[1])
