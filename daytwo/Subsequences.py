# A="TCS"
# B="Tata Service"
A="infy"
B="infosys"
def isSubSequence(A,B):
    p=0
    for i in range(len(B)):
        if B[i]==A[p]:
            p+=1
        if p==len(A):
            return 1
    return 0

print(isSubSequence("tcs","tata service"))
print(isSubSequence("infy","infosys"))
print(isSubSequence("cognizant technology","cts"))
print(isSubSequence("tcs","tata consultancy service"))