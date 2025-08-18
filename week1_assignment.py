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
    
#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def three_sum(nums:list[int]) -> list[int] | None:
    """
    Given an array of integers, return the indices of three numbers that add up to 0.

    :param nums: List of integers.
    :return: List containing indices of the three numbers that add up to 0, or None if no such triplet exists.
    """
    

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]





