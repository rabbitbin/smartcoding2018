# Question 2

# Design a phone book program. In this program, we can
# think of a phone book as a collection of friends,
# associates, family with their information such as a
# telephone number, email address, name and location.
# Design a simple program that gets the names from a
# random list like:
# names = [‘peter’, ‘mary’, ‘jane’]
# location = [‘stockholm’, ‘goteborg’, ‘helsingborg’]
# This is my answer:
# def phoneBook(names, location):
# return dict(zip(names, location)

## SOLUTION: 

# Lists of my phone book
names = ['Stella','May','Bo','Ella','Johan']
phones = ['+1-2345876900','+852-89276384','+61-374889021','+33-367676789','+46-7800213466']
emails = ['stellafishes@yahoo.com','mayhong@gmail.com','2188bo@hotmail.com','mrsella@gmail.com','jandersson@sgi.se']
countries = ['USA','Hong Kong','Australian','France','Sweden']

# function for phone book
def friends_list(names, phones, emails, countries):
  friends_dict = {}  # an empty dictioinary
  for i in range(len(names)): # for loop over the length of names
    friends_dict[names[i]] = phones[i], emails[i], countries[i]  # set key, value for the dictionary
  print(friends_dict) # show the lists of my phone book in dictionary
friends_list(names, phones, emails, countries) # convert lists into dictionaries

 