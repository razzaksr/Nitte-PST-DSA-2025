def prefixSum(origin,result,index):
    if index == 0: result[0] = origin[0]
    else:
        prefixSum(origin,result,index-1)
        result[index] = result[index-1]+origin[index]

# source = [23,12,98,45,18,45,12,98]
# output = [0]*len(source)
# prefixSum(source,output,len(source)-1)

def fixSumViaDC(origin,result):
    if len(origin)==1:
        result.append(origin[0])
    else:
        fixSumViaDC(origin[1:],result)
        # print(len(origin),origin[0])
        result.append(result[len(origin)-2]+origin[0])

source = [23,12,98,45,18,45,12,98]
output = []
fixSumViaDC(source[::-1],output)
print(output)
output = []
fixSumViaDC(source,output)
print(output)





