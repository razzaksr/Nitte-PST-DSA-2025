# s="222.111.111.111"
s="5555..555"
s="0.0.0.0255"
def validIP(s):
    s=s.split(".")
    if len(s)!=4:
        return False
    for c in s:
        if len(c)>3 or int(c)>255:
            return False
    return True

print(validIP(s))