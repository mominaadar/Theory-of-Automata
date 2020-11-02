
########## MOMINA ATIF DAR P18-0030

import re

file = open('logs.txt','r')
string=""
for line in file:
    string = line+string

pattern = re.compile(r'(20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])')

m = pattern.findall(string)

print(m)
