arr=[20,0,19,5,0,3,10,0,2]
def func():
    valid=0
    for index in range(len(arr)):
        if arr[index]!=0:
            arr[valid]=arr[index]
            valid+=1
    arr[valid:]=[0]*(len(arr)-valid)
func()
print(arr)