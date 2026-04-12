"""Part 5: Sets - Unique Collections
What is a Set?
A set is an unordered collection of unique items.
Key Properties:
• No duplicates - automatically removed
• Unordered - no indexing
• Fast membership testing
• Mathematical set operations"""

# Creating sets
fruits = { " apple " , " banana " , " orange " }
numbers = {1 , 2 , 3 , 4 , 5}

# Duplicates automatically removed !
scores = {85 , 92 , 78 , 85 , 92}
print ( scores ) # {78 , 85 , 92} ( only unique values )

# Empty set ( can ’t use {} - that ’s a dict !)
empty_set = set ()  #can use() only not {}

# Convert list to set ( remove duplicates )
numbers = [1 , 2 , 2 , 3 , 3 , 3 , 4 , 5 , 5]
unique = set ( numbers )
print ( unique ) # {1 , 2 , 3 , 4 , 5}

"""Set Operations - Mathematical!"""
set1 = {1 , 2 , 3 , 4}
set2 = {3 , 4 , 5 , 6}
# Union - all items from both sets
print ( set1 | set2 ) # {1 , 2 , 3 , 4 , 5 , 6}
print ( set1 . union ( set2 ) ) # Same thing
# Intersection - items in BOTH sets
print ( set1 & set2 ) # {3 , 4}
print ( set1 . intersection ( set2 ) ) # Same thing

# Difference - items in set1 but NOT in set2
print ( set1 - set2 ) # {1 , 2}
print ( set1 . difference ( set2 ) ) # Same thing

# Symmetric difference - items in either , but not both
print ( set1 ^ set2 ) # {1 , 2 , 5 , 6}
print ( set1 . symmetric_difference ( set2 ) ) # Same thing


"""Practical Set Uses"""
# Remove duplicates from list
numbers = [1 , 2 , 2 , 3 , 3 , 3 , 4 , 5 , 5]
unique = list ( set ( numbers ) )
print ( unique ) # [1 , 2 , 3 , 4 , 5]

# Fast membership testing ( very fast ! - O (1) )
valid_users = { " alice " , " bob " , " charlie " }
if " alice " in valid_users :
 print ( " Access granted ! " )

# Find common elements
alice_courses = { " CS101 " , " MATH201 " , " PHYS101 " }
bob_courses = { " CS101 " , " CHEM101 " , " MATH201 " }
common = alice_courses & bob_courses
print ( f" Common courses : { common } " )
# { ' CS101 ', ' MATH201 ' }

# Find unique visits
visited_cities = { " NYC " , " LA " , " Chicago " }
new_city = " Boston "
if new_city not in visited_cities :
 visited_cities . add ( new_city )
print ( f" Added { new_city }! " )


"""Set Methods"""
fruits = { " apple " , " banana " }
# Add single item
fruits . add ( " orange " )
print ( fruits ) # { ' apple ', ' banana ', ' orange ' }

# Add multiple items
fruits . update ([ " grape " , " kiwi " ])
print ( fruits )

# Remove items
fruits . remove ( " banana " ) # Error if not found
fruits . discard ( " mango " ) # No error if not found

# Pop random item ( sets are unordered !)
item = fruits . pop ()
print ( f" Removed : { item } " )

# Clear all items
fruits . clear ()