def bin(trends, skill, begin, end):
    if begin > end: return -1
    else:
        mid = begin+(end-begin)//2
        if trends[mid] == skill: return mid+1
        elif trends[mid] < skill: return bin(trends,skill,mid+1,end)
        else: return bin(trends,skill,begin,mid-1)

trends = ["Java developer", "cloud architect", "data analyst", "devops engineer" ,"full stack developer", "network associate"]
print(bin(trends,"Data analyst",0,len(trends)-1))
print(bin(trends,"data analyst",0,len(trends)-1))
print(bin(trends,"network associate",0,len(trends)-1))