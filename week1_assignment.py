#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]
from operator import itemgetter

def two_sum(nums: list[int], target: int) -> list | None:
    """
   Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

   :param nums: List of integers.
   :param target: Target integer to find the sum.
   :return: List containing indices of the two numbers that add up to `target`, or None if no such pair exists.
   """
    
    if len(nums) < 2:
        print("The list isn't big enough.")
        
    else:
        for number_1 in nums:
            
            first_value_index = nums.index(number_1)
            first_value = number_1

            for number_2 in nums:
                if number_2 != first_value:
                    final_value = first_value + number_2
                    if final_value == target:
                        second_value_index = nums.index(number_2)
                        nums_index = []
                        nums_index = nums_index.append(first_value_index)
                        nums_index = nums_index.append(second_value_index)
                        return nums_index






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
    char_pos_index = 0
    smallest_word_len = 0
    char_similar = []
    for word in list_of_words:
        if word[0]:
            smallest_word_len = len(word)
        else:
            if smallest_word_len > len(word):
                smallest_word_len = len(word)

            else:
                continue
    looper=0
    index_get=0
    final_output_string=""
    char_similar = []
    while True:

        word = list_of_words[index_get]
        char_similar= char_similar.append(word[0:index_get])
        looper=looper+1
        if looper == len(list_of_words):
            looper=0
            index_get = index_get + 1
            final_output_string = word[0:index_get]
            continue

        if len(set(char_similar)) != 1:
            break


    return final_output_string

    

    
#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def three_sum(nums:list[int]) -> list[int] | None:
    """
    Given an array of integers, return the indices of three numbers that add up to 0.

    :param nums: List of integers.
    :return: List containing indices of the three numbers that add up to 0, or None if no such triplet exists.
    """
    negative = 0
    seen = {}
    for n in nums:
         number_1 = n
         number_1_index =
         
         for m in nums:
             number_2 = m
             negative = -1(number_1 + number_2)

             if negative in seen:
                 return [seen[negative], m]
             
             else:
                 seen[nums[m]] = [n , m]

    

             
    

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]
def reverse_order_list(list_of_items):
    looper = 0
    if len(list_of_items)% 2 == 0:
        looper_lim = len(list_of_items)/2

    else:
        looper_lim = int(len(list_of_items)/2)

    while looper < looper_lim:
        temp = list_of_items[looper]
        list_of_items[looper] = list_of_items[-1(looper) -1]
        list_of_items[-1(looper) -1] = temp

    return list_of_items



    





