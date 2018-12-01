
# Question 3
# An ICA supermarket attendant works every day selling to customers. They
# have a business where each item you buy, mjolk, Pannkakor, Bröd, Paj, and
# everything there costs a positive number of Kroner (integers). If bröd costs
# 22 kroner. There is no item in ICA that costs a decimal value like 10.13 kr
# (VAT tax is included in the amount already).
# Kroner change can be provide in 1 kr, 2kr, 5kr and 10kr.
# Write a function in Python that takes in two arguments will return the correct
# change to the customer with the smallest possible number of coins (or bills if
# paper money is used).
# def getChange(costOfItem, amountPaid):
# replace with your code


## SOLUTION 1: Return total amount of the change. I tried to using for loop and 
# if statement but it didn't work so far. This is so far I have reached for now.

# FINAL SOLUTION:  
# check also if there paid enough money for a change

## FINAL SOLUTION
def getChange(costOfItem, amountPaid): # create a function
    if costOfItem < amountPaid:  # check if there are enough moneh for a change
        coins = amountPaid - costOfItem # caluate how much is the change
    else:
       print ("You don't have enough money!!\n") # if there are no money or not enough money for a change, 
       return False # stop function and give a error message
      
    ten = coins // 10  # divide 10 to check for value of 10kr
    five = coins % 10 // 5  # check how much remainder efter divided 10 and divid it by 5 (5kr)
    two = coins % 10 % 5 // 2 # and so on for 2 kr
    one = coins % 10 % 5 % 2 // 1 # removed // 1 because no need for it, just the same number
    
    # output for the change we have to make
    print("The change of coins for", coins, "kr are:") 
    print("10 kr: ", ten)
    print("5 kr: ", five) 
    print("2 kr: ", two)
    print("1 kr: ", one)
    print()

getChange(46, 100)
getChange(28, 100)
getChange(25, 20)  # test for not getting enough money for a change
getChange(124, 150) 
    


## SOLUTION 2: with out checking if there are money remained for a change.

# def getChange(costOfItem, amountPaid):
#     if costOfItem < amountPaid:
#         coins = amountPaid - costOfItem
#     ten = coins // 10
#     five = coins % 10 // 5
#     two = coins % 10 % 5 // 2
#     one = coins % 10 % 5 % 2 // 1
    
#     print "The change of coins for", coins, "are:"
#     print "Ten kronar: ", ten , "kr"
#     print "Five kronar: ", five , "kr"
#     print "Two kronar: ", two , "kr"
#     print "One kronar: ", one , "kr"
#     print
# getChange(22, 50) 