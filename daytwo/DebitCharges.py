def charges(statement):
    if len(statement) < 2:return
    else:
        debit_count=0
        for index in range(len(statement)):
            if statement[index]<statement[index-1]:debit_count+=1
        debit_count-=3
        if debit_count>0:statement[len(statement)-1] -= (debit_count*24)
    print(statement)

charges([900,1200,5600,120,450,670,100,10000,400,120])
charges([900,1200,5600,10000])
charges([5600,900,670,450,400,120])