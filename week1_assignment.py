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
        print("The list size is smaller than 2.")
        return
        
    else:
        for i in nums:
            
            first_value_index = nums.index(i)
            first_value = i

            for j in nums:
                if j != first_value:
                    final_value = first_value + j
                    if final_value == target:
                        second_value_index = nums.index(j)
                        nums_index = []
                        nums_index = nums_index.append(first_value_index)
                        nums_index = nums_index.append(second_value_index)
                        return nums_index
                    
                    elif j < nums & i < nums:
                        continue

                    else:
                        print("No two numbers in the list add up to the target number")

                else:
                    continue
                        
                    
                






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
    smallest_word_len = 0
    char_similar = []
    if len(list_of_words) == 0:
        print("The list is empty. Please feed a list with string data.")
        exit

    elif len(list_of_words) == 1:
        return list_of_words[0]
    
        
    else:

        for word in list_of_words:
            if word[0]:
                smallest_word_len = len(word)
            else:
                if smallest_word_len > len(word):
                    smallest_word_len = len(word)

                else:
                    continue
        iterator=0
        extract_index=0
        final_output_string=""
        char_similar = []
        while True:

            word = list_of_words[extract_index]
            char_similar= char_similar.append(word[0:extract_index])
            iterator=iterator+1
            if iterator == len(list_of_words):
                iterator=0
                extract_index = extract_index + 1
                final_output_string = word[0:extract_index]
                continue

            elif len(set(char_similar)) != 1:
                break

            else:
                print("The list had no matching characters.")
                exit


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
    if len(nums) < 3:
        print(f"You have a list of size {len(nums)}. Minimum size of the list shoud be 3.")
        exit

    else:

        negative = 0
        seen = {}
        for n in nums:
            first_output_value = n
            
            for m in nums:
                second_output_value = m
                negative = -1(first_output_value + second_output_value)

                if negative in seen:
                    return [seen[negative], m]
                
                else:
                    seen[nums[m]] = [n , m]

        
        if n and m == len(nums):
            print("No 3 numbers in the listed, the sum of which was 0 were present.")
            exit


        

             
    

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]
def reverse_order_list(list_of_items):
    interator = 0

    if len(list_of_items) == 0:
        print("You have an empty list.")
        exit
    elif len(list_of_items)% 2 == 0:
        max_iterations = len(list_of_items)/2

    else:
        max_iterations = int(len(list_of_items)/2)

    while interator < max_iterations:
        temp = list_of_items[interator]
        list_of_items[interator] = list_of_items[-1(interator) -1]
        list_of_items[-1(interator) -1] = temp

    return list_of_items



    





