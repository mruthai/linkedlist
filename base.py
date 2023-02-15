
class LiliNode:
  # class node to store value and prep for next through initializer below
  def __init__(self, val):
    self.val = val
    self.next = None

a = LiliNode('A')
b = LiliNode('B')
c = LiliNode('C')
d = LiliNode('D')

a.next = b
b.next = c
c.next = d

def linked_list_values(head):
  """function to add values to nodes into list or an 'array' """
  values = []
  current = head
  while current is not None:
    current.val.append()
    """It's important to stay current and not look ahead"""
    current = current.next
    return values
  
def remove_node(head, target_val):
  """function to remove a target node from array"""
  if head.val == target_val:
    return head.next

  current = head
  prev = None
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head


def print_llist(head):
  current = head
  while current is not None:
    print(current.val)
    current = current.next



