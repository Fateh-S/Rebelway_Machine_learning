#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]


def two_sum(nums: list[int], target: int) -> list | None:
    """
   Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

   :param nums: List of integers.
   :param target: Target integer to find the sum.
   :return: List containing indices of the two numbers that add up to `target`, or None if no such pair exists.
   """
    if len(nums) < 2:
        raise ValueError('Array must contain at least two elements.')

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    print(f'No two numbers add up to {target}.')

#Time and space complexity: O(n^2), O(1)

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def find_most_common_prefix(list_of_words: list[str]) -> str | None:
    """
    Given a list of strings, find the most common longest prefix among them.

    :param list_of_words: List of strings to evaluate.
    :return: The longest common prefix string.
    """
    if not list_of_words:
        raise ValueError("The list of strings cannot be empty.")

    list_of_words.sort(key=len)
    for i in range(len(list_of_words[0])):
        for word in list_of_words[1:]:
            if word[i] != list_of_words[0][i]:
                return list_of_words[0][:i]


#Time and space complexity: O(n * m), O(1)

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def three_sum(nums:list[int]) -> list[int] | None:
    """
    Given an array of integers, return the indices of three numbers that add up to 0.

    :param nums: List of integers.
    :return: List containing indices of the three numbers that add up to 0, or None if no such triplet exists.
    """
    if len(nums) < 3:
        raise ValueError("Array must contain at least three elements.")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    return [i, j, k]
    print("No three numbers add up to 0.")

#Time and space complexity: O(n^3), O(1)

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

def print_list(node):
    while node:
        print(node.data)
        node = node.next

def reverse_list(node: Node) -> Node:
    """
    Given a singly linked list, reverse the nodes of the linked list.

    :param node: Head node of the linked list.
    :return: New head node of the reversed linked list.
    """
    prev_node = None
    current_node = node

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

reversed_list = reverse_list(head)
print_list(reversed_list)

#Time and space complexity: O(n), O(1)




