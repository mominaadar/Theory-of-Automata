
########## MOMINA ATIF DAR P18-0030

import re

file = open('data.txt','r')
l = []
for line in file:

    pattern = re.compile(r'(^[a-z0-9_.]+@+[(?=.*gmail)(?=.*hotmail)(?=.*yahoo)(?=.*outlook)]+.+[com]{3})')
   # pattern = re.compile(r'([a-z0-9_.]+)@(gmail|hotmail|yahoo|outlook)*(.com)')
    m = pattern.findall(line)

    print(m)
