import os

def find_word_in_file(word):
    for root, dir, files in os.walk('/home/ziv/'):
        for f in files:
            try:
                with open(f, 'r') as file:
                    contents = file.read()
                    if word in contents:
                        print(file.name)
            except:
                continue
                    

find_word_in_file('galitzer')