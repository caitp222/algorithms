class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def insert_sorted(node, head_ref):
    if node.data < head_ref.data:
        node.next = head_ref
    else:
        while head_ref.next != None:
            if node.data > head_ref.data and node.data < head_ref.next.data:
                node.next = head_ref.next
                head_ref.next = node
            head_ref = head_ref.next

def print_list(head_ref):
    while head_ref.next != None:
        print head_ref.data
        head_ref = head_ref.next


item6 = Node(6)
item5 = Node(5, item6)
item3 = Node(3, item5)
item2 = Node(2, item3)
head = Node(1, item2)

item4 = Node(4)

print_list(head)
insert_sorted(item4, head)
print "\n\n"
print_list(head)
