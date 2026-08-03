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


if __name__ == '__main__':
  ll = Linked_list
  ll.print(35)
  ll.print(42)
