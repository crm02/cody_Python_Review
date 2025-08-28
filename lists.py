#Combining two lists

movie_list = ['The Batman',"Inception",
              "The Prestige","Batman",
              "Batman again"]

rating_list = [5, 4, 3, 5, 1]

#Can combine these two lists into a single list of tuples using Pythons zip function
print(list(zip(movie_list,rating_list)))
# The Zip function returns a zip object, whilst the list function returns it as a list


###############################################################
# Finding duplicates in a list
# Done by using a set() data structure. 
# A set cannot contain duplicates 

# How to create a set and add data to it

a_set = set()
a_set.add('Kanye West')
a_set.add('Kanye West')
a_set.add('Hawkins')
a_set.add('Dr. Pepper')
print(a_set)
# This set only has a length of 3 because it does not accept the second Kanye west
# Function to find duplicates in a list
def find_dups(iterable):
    dups = []
    a_set =set()

    for item in iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 =len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = ["Michael","Susan","Jack","Michael"]

dups = find_dups(a_list)
print(dups)