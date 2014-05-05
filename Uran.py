#!/usr/local/bin/python3
import re
import pdb
def showmatch(match):
        if match is None:
                return None
                print("doesn't work")
        return "Match: %r, groups %r" %(match.group(), match.groups())
        print("Match: %r, groups %r" %(match.group(), match.groups()))
        print("hi")

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

number = re.compile(r'^[a2-9tjqk]{5}$')
valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))
showmatch(number.match("akt5q"))
#pdb.set_trace()
showmatch(number.match("ads"))

text = "He 30 1 400 s"
allmatch =re.findall(r'\d*', text)
alls = []
for _ in allmatch:
        if _ is not None:
                alls.append(_)

print(allmatch)
print(alls)

#with open(r'/users/abrick/resources/urantia') as lib:
#       number = []
#       words = [line.split() for line in lib]
#       n = re.compile(r"\d*")
#       for word in words:
#               p = n.match(str(word))
#               if len(str(p)) is not 0:
#                       number.append(p.group())
#       print(number)
