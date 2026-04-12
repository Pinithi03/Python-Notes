"""What is a Dictionary?
A dictionary stores data as key-value pairs for instant lookups.
Think of a real dictionary:
• WORD (key) → DEFINITION (value)
• STUDENT NAME (key) → GRADE (value)
• USERNAME (key) → PASSWORD (value)

Why Dictionaries?
• Fast lookups - O(1) time complexity (instant!)
• Meaningful keys - use names instead of indices
• Flexible data - values can be any type"""

#Creating Dictionaries
# Empty dictionary
empty = {}

# Dictionary with data
student = {
" name " : " Alice " ,
" age " : 20 ,
" gpa " : 3.8 ,
" major " : " Computer Science "
}
# Simple example
prices = {
" apple " : 1.50 ,
" banana " : 0.80 ,
" orange " : 2.00
}
# Values can be any type !
person = {
" name " : " Bob " ,
" age " : 25 ,
" skills " : [ " Python " , " Java " , " C ++ " ] , # List as value !
" is_student " : False
}


#Accessing Dictionary Values
#Square brackets raise KeyError if key doesn’t exist.
#.get() method returns default value instead of error.
student = {
" name " : " Alice " ,
" age " : 20 ,
" gpa " : 3.8
}

# Method 1: Square brackets - RISKY !
print ( student [ " name " ]) # " Alice " - works
# print ( student [" email "]) # KeyError ! - program crashes

# Method 2: . get () - SAFE !
print ( student . get ( " name " ) ) # " Alice "
print ( student . get ( " email " ) ) # None ( no error !)
print ( student . get ( " email " , " N / A " ) ) # " N / A " ( custom default )

#Modifying Dictionaries
student = {
" name " : " Alice " ,
" age " : 20 ,
" gpa " : 3.8
}

# Update existing value
student [ " age " ] = 21
print ( student [ " age " ]) # 21
# Add new key - value pair
student [ " email " ] = " alice@email . com "
print ( student )
# {" name ": " Alice " , " age ": 21 , " gpa ": 3.8 , " email ": "..."}

# Delete key - value pair
del student [ " gpa " ]
print ( student )
# Remove and return value
email = student . pop ( " email " )
print ( email ) # " alice@email . com "

"""Looping Through Dictionaries"""
#Ex1:
student = {
" name " : " Alice " ,
" age " : 20 ,
" gpa " : 3.8 ,
" major " : " CS "
}

# Loop through keys only ( default )
for key in student :
 print ( key )
# name , age , gpa , major
# Loop through keys explicitly
for key in student . keys () :
 print ( key )

# Loop through values only
for value in student . values () :
 print ( value )
# Alice , 20 , 3.8 , CS

# Loop through key - value pairs ( most useful !)
for key , value in student . items () :
 print ( f" { key }: { value } " )
# name : Alice
# age : 20
# gpa : 3.8
# major : CS

#Ex2:
# Count votes
votes = [ " Alice " , " Bob " , " Alice " , " Charlie " , " Alice " , " Bob " ]

# Method 1: Manual counting
vote_count = {}
for name in votes :
 if name in vote_count :
  vote_count [ name ] += 1
else :
 vote_count [ name ] = 1

print ( vote_count )
# { ' Alice ': 3 , ' Bob ': 2 , ' Charlie ': 1}

# Method 2: Using . get () ( cleaner !)
vote_count = {}
for name in votes :
  vote_count [ name ] = vote_count . get ( name , 0) + 1

print ( vote_count )
# { ' Alice ': 3 , ' Bob ': 2 , ' Charlie ': 1}


"""Dictionary Methods"""
student = { " name " : " Alice " , " age " : 20 , " gpa " : 3.8}

# Check if key exists
print ( " name " in student ) # True
print ( " email " in student ) # False

# Get all keys as list
keys = list ( student . keys () )
print ( keys ) # [ ’ name ’, ’ age ’, ’ gpa ’]

# Get all values as list
values = list ( student . values () )
print ( values ) # [ ’ Alice ’, 20 , 3.8]

# Get all key - value pairs as list of tuples
items = list ( student . items () )
print ( items )
# [( ’ name ’, ’ Alice ’) , ( ’ age ’, 20) , ( ’ gpa ’, 3.8) ]

# Clear all items
student . clear ()
print ( student ) # {}


"""Nested Dictionaries"""
# Dictionary of dictionaries
students = {
" alice " : {
" age " : 20 ,

" gpa " : 3.8 ,
" major " : " CS "
} ,
" bob " : {
" age " : 21 ,
" gpa " : 3.5 ,
" major " : " Math "
}
}

# Access nested values
print ( students [ " alice " ][ " gpa " ]) # 3.8
print ( students [ " bob " ][ " major " ]) # " Math "

# Modify nested values
students [ " alice " ][ " age " ] = 21

# Iterate through nested dict
for name , info in students . items () :
 print ( f" { name }: " )
for key , value in info . items () :
  print ( f" { key }: { value } " )