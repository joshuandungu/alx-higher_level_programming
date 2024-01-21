#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store True or False values
    result_list = []

    # Iterate through each element in the original list
    for number in my_list:
        # Check if the number is a multiple of 2
        is_multiple_of_2 = number % 2 == 0

        # Append True or False to the result list
        result_list.append(is_multiple_of_2)

    return result_list
