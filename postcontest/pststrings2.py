def sovle(s,t):
    d={}
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]]!=t[i]:
                return False
        else:
            d[s[i]]=t[i]
    return True
        
print(sovle('aba','abb'))
print(sovle('egg','att'))
        