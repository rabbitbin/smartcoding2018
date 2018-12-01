# Question 1
# Design a function within a Python script that takes in a list of numbers, for
# example [1,2,3,4,5] and returns another list with each number multiplied by 2. 


# SOLUTION:
def multiply_by_two(a_list): # function to check a list of numbers
  values_to_return = [] # start as the empty list
  for i in a_list: # loop over each number in the list
    values_to_return.append( i * 2 ) # each number multiplied by 2
  return values_to_return # return the list

x = [1,2,3,4,5]  
print(multiply_by_two(x)) 

# print(multiply_by_two([1,2,3,4,5]))