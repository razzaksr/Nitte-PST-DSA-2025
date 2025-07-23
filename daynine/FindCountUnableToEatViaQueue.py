from collections import deque
def findCount(students, sandwiches):
    students = deque(students)
    count = 0
    while sandwiches and count < len(students):
        if sandwiches[0] == students[0]:
            sandwiches.pop(0)
            students.popleft()
            count = 0
        else:
            count+=1
            students.append(students.popleft())
    return count
print(findCount([1,1,0,0],[0,1,0,1]))
print(findCount([1,1,1,0,0,1],[1,0,0,0,1,1]))