# https://www.interviewcake.com/question/ruby/reverse-linked-list
# inplace reverse linked list

class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_linked_list(head_ref):
    arr = [head_ref]
    while head_ref.next != None:
        arr.append(head_ref.next)
        head_ref = head_ref.next
    while len(arr) > 0:
        current = arr[-1]
        del(arr[-1])
        if len(arr) == 0:
            current.next = None
        else:
            current.next = arr[-1]
    return head_ref

def print_list(head_ref):
    while head_ref != None:
        print head_ref.data
        head_ref = head_ref.next
    print "\n"

item6 = LinkedListNode(6)
item5 = LinkedListNode(5, item6)
item4 = LinkedListNode(4, item5)
item3 = LinkedListNode(3, item4)
item2 = LinkedListNode(2, item3)
item1 = LinkedListNode(1, item2)

print_list(item1)
print_list(reverse_linked_list(item1))
