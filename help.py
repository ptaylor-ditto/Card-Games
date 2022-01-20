s = "ab12cd34ef56gh78ij90"

newstring = s.translate({ord(i): None for i in 'abc'})

print(newstring)