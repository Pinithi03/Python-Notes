"""Error Handling Essentials
The Problem: Programs Crash!"""
# Without error handling - program crashes !
age = int ( input ( " Enter your age : " ) ) # User types " abc "
# ValueError : invalid literal for int () with base 10: ’ abc ’
# With error handling - program survives !
try :
    age = int ( input ( " Enter your age : " ) )
    print ( f" Next year you ' ll be { age + 1} " )
except ValueError :
    print ( " Please enter a valid number ! " )
# Program continues running !
print ( " No crash ! " )

#try / except Syntax
try :
# Code that MIGHT raise an exception
# If this succeeds , skip the except block
    risky_operation ()
except SpecificError :
# This runs ONLY if that specific error occurs
    handle_the_error ()
# Program continues normally

"""Common Exception Types"""
#ValueError          Wrong value for conversion         int("abc")
#TypeError           Wrong type in operation            "hello" + 5
#KeyError            Missing dictionary key             dict["missing"]
#IndexError          List index out of range            list[999]
#ZeroDivisionError   Dividing by zero                    10 / 0
#FileNotFoundError   File doesn’t exist                 open("missing.txt")

#Multiple except Blocks
# Handle different errors differently
def safe_divide (a , b ) :
    try :
        result = a / b
        return result
    except ZeroDivisionError :
        print ( " Cannot divide by zero ! " )
        return None
    except TypeError :
        print ( " Both arguments must be numbers ! " )
    return None
safe_divide (10 , 0) # Cannot divide by zero !
safe_divide ( " 10 " , 2) # Both arguments must be numbers !

#The Complete try/except/else/finally
try :
# Code that might fail
    number = int ( input ( " Enter a number : " ) )
    result = 100 / number
except ValueError :
# Runs if ValueError occurs
    print ( " Not a valid number ! " )
except ZeroDivisionError :
# Runs if ZeroDivisionError occurs
    print ( " Cannot divide by zero ! " )
else :
# Runs ONLY if NO exception occurred
    print ( f" Result : { result } " )
finally :
# ALWAYS runs , error or not ( cleanup code )
    print ( " Operation complete . " )
    
"""When to Use Each Part
• try: Wrap code that might raise an exception
• except: Handle specific errors gracefully
• else: Code that should only run on success
• finally: Cleanup code (closing files, connections)"""

#Raising Your Own Exceptions
# Use raise to create your own errors
def set_age ( age ) :
 if age < 0:
    raise ValueError ( " Age cannot be negative ! " )
 if age > 150:
    raise ValueError ( " Age seems unrealistic ! " )
 return age
# Catching raised exceptions
try :
    my_age = set_age ( -5)
except ValueError as e :
    print ( f" Error : { e } " )
# Output : Error : Age cannot be negative !

#Input Validation Pattern
# The " keep asking " pattern - very common !
def get_valid_number ( prompt ) :
    """ Keep asking until user enters a valid number """
    while True :
        try :
            return int ( input ( prompt ) )
        except ValueError :
            print ( " Invalid ! Please enter a number . " )
    print ( " Invalid ! Please enter a number . " )
def get_number_in_range ( prompt , min_val , max_val ) :
    """ Get a number within a specific range """
    while True :
        try :
            number = int ( input ( prompt ) )
            if min_val <= number <= max_val :
                return number
            print ( f" Must be between { min_val } and { max_val }! " )
        except ValueError :
            print ( " Invalid ! Please enter a number . " )

# Usage
age = get_valid_number ( " Enter your age : " )
score = get_number_in_range ( " Score (0 -100) : " , 0 , 100)