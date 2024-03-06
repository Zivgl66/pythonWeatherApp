import os # import for operating system file search and stat module
import sys # import for the arguments in command line
# exercise5:

'''
Find the file path of a given file name
'''
def find_files(filename):
    for root, dirs, files in os.walk("/"):
        if filename in files:
            return os.path.join(root, filename)
    return None

'''
if File was found in the system, check it's x permissions, if none, add x to owner and group permissions
'''
def find_and_perm(file):
    file_path = find_files(file)
    if file_path:
        if not os.access(file, os.X_OK):
            os.chmod(file_path, os.stat(file_path).st_mode | os.stat.S_IXGRP | os.stat.S_IXUSR)
            print("File Permissions changed!")
        else:
            print("File has permissions!")
    else:
        print("File Not Found!")


find_and_perm(sys.argv[1])
