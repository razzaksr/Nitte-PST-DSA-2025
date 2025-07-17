# ip="192.1.1.17"
import re
# ip=input()
# ip = "192.168.02.7"
ip = "192.1.1.17"
def validate(each):
    pattern = r'^(\d{1,3})$'
    if not re.match(pattern,each) or (len(each)>1 and each.startswith('0')) or not 0<=int(each)<=255:
        return False
    return True
octet=ip.split(".")
flag = True
for i in octet:
    flag = validate(i)
    if not flag: break
print(flag)