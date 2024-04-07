import sys

def reverse_lines(file):
    try:
        with open(file, "r+") as f, open("./newfile.txt", "w+") as nf:
            lines = f.readlines()
            lines = lines[::-1]
            for line in lines:
                nf.write(line)
    except:
        print('failed to open text')
        
reverse_lines(sys.argv[1])

#   bash
#   cat txt.txt | sort --reverse > newfile.txt