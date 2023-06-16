import sys
import re


pattern = r".+\.txt$"

if len(sys.argv) == 1:
    print("Hello world")

elif len(sys.argv) == 2 and re.match(pattern, sys.argv[1]):
    with open(sys.argv[1]) as f:
        text = f.read()
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word,0) + 1
    print(count)

elif len(sys.argv) == 2:
    print(sys.argv[1][::-1])

else:
    print("Wrong format!")