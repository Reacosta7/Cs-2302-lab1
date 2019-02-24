#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     


#Start of code
    #is sorted
def IsSorted(L):
    temp = L.head
    while temp is not None:
        if temp.item > temp.next.item:
            return False
    temp = temp.next
    #BubbleSort
def bubbleSort(L):
    if IsEmpty(L):
        return None
    temp = L.head
    listOrdered = False
    while listOrdered is False:
        listOrdered = True
        while temp.next is not None:
            if temp.item > temp.next.item:
                temp2 = temp.item
                temp.item = temp.next.item
                temp.next.item = temp2.item
                listOrdered = False
            temp = temp.next
    return L
    #Merge Sort
def mergeSort(L):
    if IsEmpty(L):
        return None
    if len(L) > 1:
        split(L)
    return L
def split(L):
    midpnt = len(L)/2
    L1 = List()
    L2 = List()
    L1.head = L.head
    temp = L1.head
    for i in midpnt:
        temp = temp.next
    L1.tail = temp #need the tail to equal to mid
    L2.head = temp.next
    L2.tail = L.tail
    mergeSort(L1)
    mergeSort(L2)
    if len(L) == 2:
        merge(L1,L2)
def merge(L1,L2):
    if IsEmpty(L1):
        return L2
    if IsEmpty(L2):
        return L1
    if L1.head.item <= L2.head.item:
        Append(L1,L2)
        return L1
    else:
        Append(L2,L1)
        return L2
    #QuickSort
def quickSort(L):
    if IsEmpty(L):
        return None
    temp = L.head
    L1 = List()
    L2 = List()
    L3 = List()
    Append(L3,temp)
    while temp is not None:
        if temp.item > temp.next.item:
            Append(L2,temp)
        else:
            Append(L1,temp)
        temp = temp.next
    quickSort(L1)
    quickSort(L2)
    return(L3)
        #QuickSort2
def quickSort2(L):
    if IsEmpty(L):
        return None
    temp = L.head
    L1 = List()
    L2 = List()
    L3 = List()
    Append(L3,temp)
    while temp is not None:
        if temp.item > temp.next.item:
            Append(L2,temp)
        else:
            Append(L1,temp)
        temp = temp.next
    return(L3)
    
L = List()
Append(L,5)
Append(L,17)
Append(L,8)
Append(L,22)
Append(L,7)
print(bubbleSort(L))
Print(L)
PrintRec(L)
PrintReverse(L)
