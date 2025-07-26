class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Links:
    def __init__(self):
        self.head = None
    # operations
    def insertNewNode(self,data):
        newNode = Node(data)
        # decide new node is head
        if not self.head: self.head = newNode
        else:
            # add at end of the link
            traverse = self.head
            while traverse.ref: traverse = traverse.ref
            traverse.ref = newNode
    def readAll(self, current=None):
        traverser = self.head if not current else current
        while traverser:
            print(traverser.data,end="->" if traverser.ref else "")
            traverser = traverser.ref
    def readBetWeen(self,start,end):
        traverser = self.head
        index = 1
        while traverser:
            if start<=index<=end: 
                print(traverser.data,end="->" if traverser.ref else "")
            traverser = traverser.ref
            index+=1
    def listIntoLinkedList(self,mylist):
        if not mylist: return
        else:
            tempHead = Node(mylist[0])
            tempCursor = tempHead
            for each in mylist[1:]:
                tempCursor.ref = Node(each)
                tempCursor = tempCursor.ref
            return tempHead
    def mergeLeftRight(self,left,right):
        select = Node(0)
        cursor = select
        while left and right:
            if left.data < right.data:
                cursor.ref = left
                left = left.ref
            else:
                cursor.ref = right
                right = right.ref
            cursor = cursor.ref
        cursor.ref = left if left else right
        return select.ref

link = Links()
link.insertNewNode(14)
link.insertNewNode(28)
link.insertNewNode(10)
link.insertNewNode(7)
# link.readAll()
# link.readBetWeen(2,4)
linked1 = link.listIntoLinkedList([1,5,8])
linked2 = link.listIntoLinkedList([2,6])
# link.readAll(linked1)
merged = link.mergeLeftRight(linked1,linked2)
link.readAll(merged)