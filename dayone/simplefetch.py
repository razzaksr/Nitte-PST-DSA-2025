experts = [
    {
        "expertId":123,
        "ctc":4,
        "role":"developer"
    },
    {
        "expertId":456,
        "ctc":9,
        "role":"project manager"
    },
    {
        "expertId":765,
        "ctc":6,
        "role":"devops engineer"
    },
    {
        "expertId":912,
        "ctc":5,
        "role":"system design engineer"
    },
    {
        "expertId":123,
        "ctc":3,
        "role":"sdet"
    }
]

# fetch ctc b/w 4-9
def fetchByCTC():
    for expert in experts:
        if expert["ctc"] >= 4 and expert["ctc"]<=9:print(expert)

def fetchByRole(role):
    for expert in experts:
        if expert['role'].startswith(role):print(expert)

def findSecondMaxCtc():
    firstMax = experts[0]
    secondMAx = experts[0]
    for expert in experts:
        if expert['ctc'] >= firstMax['ctc']:
            secondMAx=firstMax
            firstMax = expert
        elif expert['ctc'] >= secondMAx['ctc'] and expert!=firstMax:
            secondMAx = expert
    
    print(secondMAx)

# fetchByCTC()
# fetchByRole('d')
# fetchByRole('p')
# fetchByRole('s')
# findSecondMaxCtc()

'''
test cases:

target: 10
[developer, devops engineer]

target: 11
[devops engineer, system design engineer]
'''

def twoSumTarget(target):
    table = {}
    for index, expert in enumerate(experts):
        subtract = target - expert['ctc']
        if subtract in table:
            return [experts[table[subtract]]['role'],experts[index]['role']]
        table[expert['ctc']]=index
    return []
print(twoSumTarget(10))
print(twoSumTarget(11))
print(twoSumTarget(15))
print(twoSumTarget(20))