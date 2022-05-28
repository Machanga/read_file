# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from itertools import count


def read_file_content(filename):
    filename = "./story.txt"
    f = open(filename, "r") 
    return f.read()
    
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words =  text.split()
    
    count = {}
    for x in words:
        if x in count:
            count[x] += 1   
        else:
            count[x] = 1
    return count

print(read_file_content(filename))
print(count_words())



