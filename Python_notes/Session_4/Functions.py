"""Part 1: Functions
What is a Function?
A function is a reusable block of code that performs a specific task. Think of it as a recipe you
can use over and over again.
Why Functions Matter:
• Avoid repetition - Write once, use many times
• Organization - Break complex problems into smaller pieces
• Maintainability - Fix bugs in one place
• Readability - Give meaningful names to operations"""

#Defining and Calling Functions
# Define a function
def greet () :
    print ( " Hello , World ! " )

# Call the function
greet () # Output : Hello , World !

"""Syntax:
• Use def keyword
• Function name follows naming rules (like variables)
• Parentheses () are required
• Colon : ends the definition line
• Indented code is the function body"""

#Parameters and Arguments
#Functions can accept input values called parameters.

# Function with parameters
def greet ( name ) :
    print ( f" Hello , { name }! " )

# Call with arguments
greet ( " Alice " ) # Output : Hello , Alice !
greet ( " Bob " ) # Output : Hello , Bob !

#Multiple Parameters:
def calculate_rectangle_area ( length , width ) :
    area = length * width
    print ( f" Area : { area } " )

calculate_rectangle_area (5 , 3) # Output : Area : 15

#Default Parameters:
def greet ( name , greeting = " Hello " ) :
    print ( f" { greeting } , { name }! " )

greet ( " Alice " ) # Output : Hello , Alice !
greet ( " Bob " , " Hi " ) # Output : Hi , Bob !
greet ( " Charlie " , " Hey " ) # Output : Hey , Charlie !

"""Return Values
Critical Concept: return vs print
print() displays output to the screen
return sends a value back to the caller (to be used in code)
You CANNOT use the result of print() in calculations!"""

# Using print - can ’t use result
def add_wrong (a , b ) :
    print ( a + b )

result = add_wrong (3 , 5) # Prints : 8
print ( result ) # Prints : None ( no value returned !)
# Can ’t use in calculations !

# Using return - can use result
def add_correct (a , b ) :
    return a + b

result = add_correct (3 , 5) # No print , but value is returned
print ( result ) # Prints : 8
total = result * 2 # Can use in calculations !
print ( total ) # Prints : 16

"""When to use which:
• Use return for calculations and processing
• Use print() for displaying information to users
2

• Most functions should return values"""