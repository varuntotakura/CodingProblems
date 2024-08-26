# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class QueueEverything:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
    
    def dequeue(self):
        if self.head:
            self.head = self.head.next
        else:
            self.tail = None
            print("No elements available")
    
    def print_first_element(self):
        if self.head:
            print(self.head.data)
        else:
            print("No elements available")
    
    def print_elements(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print("No elements available")
            
q = int(input())
qe = QueueEverything()
for i in range(q):
    t = input()
    a = t.split(" ")
    t = a[0]
    if t == '1':
        ele = a[1]
        qe.enqueue(ele)
    elif t == '2':
        qe.dequeue()
    elif t == '3':
        qe.print_first_element()
