def dispense(denomination, required, count):
    if not denomination or required<=0:return -1 if required>0 else count
    else:
        currentDenom = denomination[0]
        if required>=currentDenom:
            required-=currentDenom
            count+=1
            return dispense(denomination,required,count)
        else: return dispense(denomination[1:],required,count)

available = [100,500,200]
print(dispense(available[::-1],1100,0))
print(dispense(available[::-1],650,0))
print(dispense(available[::-1],8700,0))
print(dispense(available[::-1],1300,0))