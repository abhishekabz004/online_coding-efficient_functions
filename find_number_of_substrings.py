def numberOfSubstrings(n) :
    return int(n * (n+1) / 2)


'''
find if a string contains certain character
'''

import re

string = "sample string"

if bool(re.match('^[AaBbCc]+$', string)):
	print(True)



