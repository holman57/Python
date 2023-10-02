from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode()
    link = head
    carry = 0
    while(l1 != None or l2 != None or carry != 0):
        digit1 = l1.val if l1 != None else 0
        digit2 = l2.val if l2 != None else 0
        sum = digit1 + digit2 + carry
        resultDigit = sum % 10
        carry = int(sum / 10)
        node = ListNode(resultDigit)
        link.next = node
        link = link.next
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None
    return head.next

def print_linked_list(list_node):
    while list_node is not None:
        yield list_node.val
        list_node = list_node.next

def main():
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    print("\nTest #1")
    l1 = ListNode(2)
    input2 = ListNode(4)
    input3 = ListNode(3)
    l1.next = input2
    input2.next = input3
    print([x for x in print_linked_list(l1)])
    l2 = ListNode(5)
    input5 = ListNode(6)
    input6 = ListNode(4)
    l2.next = input5
    input5.next = input6
    print([x for x in print_linked_list(l2)])
    print([x for x in print_linked_list(addTwoNumbers(l1, l2))])


    # Input: l1 = [0], l2 = [0]
    # Output: [0]
    # print("\nTest #2")
    # l1 = LinkedList()
    # input1 = ListNode(0)
    # l1.head = input1
    # l1.tostring()
    # l2 = LinkedList()
    # input2 = ListNode(0)
    # l2.head = input2
    # l2.tostring()

    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    # print("\nTest #3")
    # l1 = LinkedList()
    # input1 = ListNode(9)
    # input2 = ListNode(9)
    # input3 = ListNode(9)
    # input4 = ListNode(9)
    # input5 = ListNode(9)
    # input6 = ListNode(9)
    # input7 = ListNode(9)
    # l1.head = input1
    # input1.next = input2
    # input2.next = input3
    # input3.next = input4
    # input4.next = input5
    # input5.next = input6
    # input6.next = input7
    # l1.tostring()
    # l2 = LinkedList()
    # input8 = ListNode(9)
    # input9 = ListNode(9)
    # input10 = ListNode(9)
    # input11 = ListNode(9)
    # l2.head = input8
    # input8.next = input9
    # input9.next = input10
    # input10.next = input11
    # l2.tostring()

if __name__ == "__main__":
    main()
