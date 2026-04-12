#What is a Tuple?
#A tuple is like a list, but immutable (cannot be changed after creation).

# Creating tuples
coordinates = (10 , 20)
rgb_color = (255 , 128 , 0)
person = ( " Alice " , 25 , " Engineer " )

# Single item tuple ( note the comma !)
single = (5 ,) # Correct
not_tuple = (5) # This is just 5 in parentheses !
# Accessing ( like lists )
print ( coordinates [0]) # 10
print ( person [2]) # " Engineer "
# Can ’t modify ( immutable !)
# coordinates [0] = 15 # TypeError !
# But can replace entire tuple
coordinates = (15 , 25) # This works


"""Tuple Unpacking
One of the most powerful features!"""
# Unpacking values from tuples
coordinates = (10 , 20)
x , y = coordinates
print ( f" x ={ x } , y ={ y } " ) # x =10 , y =20


# Multiple assignment
name , age , job = ( " Alice " , 25 , " Engineer " )
print ( f" { name } is { age } and works as { job } " )

# Swapping values ( elegant !)
a , b = 5 , 10
a , b = b , a # Swap using tuple unpacking
print (a , b ) # 10 , 5

# Return multiple values from function
def get_student () :
 return ( " Bob " , 22 , 3.7) # Returns a tuple
name , age , gpa = get_student ()

"""Tuple Methods"""
numbers = (1 , 2 , 3 , 2 , 4 , 2 , 5)

# Only 2 methods !
print ( numbers . count (2) ) # 3 ( appears 3 times )
print ( numbers . index (4) ) # 4 ( index of first 4)

# Can still iterate , slice , etc .
for num in numbers :
 print ( num )

print ( numbers [1:4]) # (2 , 3 , 2)
print ( len ( numbers ) ) # 7