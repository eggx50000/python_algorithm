class Node:
    def __init__(self,value,next_Node=None):
        self.value=value
        self.next_Node=next_Node
class node_iter:
     def __init__(self,list):
         self.list=list
         self.now=self.list.head
         
         
            
     def __iter__(self):
         return self
     def __next__(self):
         if self.now==None:
             raise StopIteration
         else:
             value=self.now.value
             self.now=self.now.next_Node
             return value
            
class List:
   
    def __init__(self,head):
        self.head=head
    def __iter__(self):
        return node_iter(self)
    
        
    def length(self):
        if self.head==None:
            return 0
        e=1
        node = self.head
        
        while True:
            if node.next_Node==None:
                return e
            else:
                e+=1
                node=node.next_Node
        
    def map(self, f):
        now=self.head
        for i in range(self.length()):
            if now==None:
                break
            else:
                now.value=f(now.value)
                now=now.next_Node
            
            
        
            
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.next_Node=node2
node2.next_Node=node3
node3.next_Node=node4
node4.next_Node=node5
joon=List(node1)
#print(joon.length())

#for i in joon:
    #print(i)

n=list(map(lambda x: x ** 3 if x % 2 == 0 else 1,joon))
for i in n:
    print(i) # 1,8,1,64,1

# 1,2,3,4.5
