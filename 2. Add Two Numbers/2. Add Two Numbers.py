"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp, carry = ListNode(-1), 0
        result = temp
        while l1 and l2:
            value = l1.val + l2.val + carry
            print(value)
            node = ListNode(value % 10)
            carry = value // 10
            l1 = l1.next
            l2 = l2.next
            temp.next = node
            temp = temp.next
        if l1:
            while l1:
                value = l1.val + carry
                node = ListNode(value % 10)
                carry = value // 10
                l1 = l1.next
                temp.next = node
                temp = temp.next
        if l2:
            while l2:
                value = l2.val + carry
                node = ListNode(value % 10)
                carry = value // 10
                l2 = l2.next
                temp.next = node
                temp = temp.next
        if carry:
            node = ListNode(carry)
            temp.next = node
        return result.next