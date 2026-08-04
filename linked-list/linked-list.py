class Node:
  def __init__(self,data=None,next = None):
    self.data = data 
    self.next = next
class Linked_list:
  def __init__(self):
    self.head = None

  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    itr = self.head
    lstr = ''
    while itr:
      lstr += str(itr.data)+ '-->' if itr.next else str(itr.data)
      itr = itr.next
    print(lstr) 

  def insert_at_beginning(self,data):
    new_node = Node(data,self.head)
    self.head = new_node
  def insert_at_end(self,data):
    if  self.head is None:
      self.head = Node(data,None)
      return
    itr = self.head 

    while itr.next:
      itr = itr.next
    itr.next = Node(data,None)  

     


if __name__ == '__main__':
  ll = Linked_list()
  ll.head = Node(62)
  ll.head.next = Node(22)
  ll.insert_at_beginning(45)
  ll.insert_at_end(89)
  ll.print()

