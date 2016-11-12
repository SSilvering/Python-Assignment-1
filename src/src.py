#===============================================================================
# Python Assignment 1
# 
# Student 1: Shai Hod - 304800402
# Student 2: Dudu Abutbul - 200913671
#===============================================================================

def Xnor(x, y):    
    """
    This function gets two boolean arguments and returns the Xnor conclusion.
    
    @param x: Boolean expression.
    @type x: Boolean expression.
    @param y: Boolean expression.
    @type y: Boolean expression.
    """
    if(x == True and y == True or x == False and y == False):
        return True
    else:
        return False
    return False

print(Xnor(9 > 5, 5 < 6))  # Executable Line for testing
#------------------------------------------------------------------------------ 

def Learn(age):    
    """
    This function identifies where the person studied according to age and returns the name of the place.
    @param age: The age of the person.
    @type age: float.
    """
    if age >= 4 and age <= 5:
        return "kindergarden"
    elif age >= 6 and age <= 14:
        return "grade_school"
    elif age >= 15 and age <= 18:
        return "high_school"
    elif age >= 19 and age <= 21:
        return "army"
    elif age >= 22 and age <= 25:
        return "sce"
    else:
        return "None"

print(Learn(4))  # Executable Line for testing
#------------------------------------------------------------------------------ 

def IsDivBy(numerator, denominator):    
    """
    This function gets numerator and denominator. The function returns true if the result of 
    the division is without a remainder, and false if the result of the division with a remainder.
    
    @param numerator: A number.
    @type numerator: float.
    @param denominator: A number.
    @type denominator: float.
    """
    
    if(denominator == 0):
        return False
    if(numerator % denominator == 0):
        return True
    else:
        return False  
    
    return False  
    
print(IsDivBy(36, 0))  # Executable Line for testing
#------------------------------------------------------------------------------ 

def Calc_pi(Iter):
    """
    This function gets the number of elements that exist in the series 
    and evaluates the value of pi according to Leibniz.
    
    @param Iter: Number of elements in series
    @type Iter: Integers 
    """
    sign, pii = 1, 0.0  # initialize parameters.
    
    for n in range(Iter):
        pii += 4 / (2 * n + 1) * sign  # evaluate specific argument in the column.
        sign *= -1  # change sign for the next iteration.
    
    return pii

print(Calc_pi(623))  # Executable Line for testing
#------------------------------------------------------------------------------ 

def Lucky_tickets():
    """
    The Function include the 6'th digits numbers , and check iterative the whole numbers
    if they are create lucky ticket.
    the condition is: if the sum of the 3 first digit's of the number equal to the 
    3 last digit's of the number.
    inside Loop the number is disassemble to digits and make the compare between the sum of
    the 3 first digit's of the number and the 3 last digit's of the number.
    if it  is equal , add it to the sum that update in the above of the loop , and return it eventually.
    """
    sum = 0
    for c in range(100000, 1000000, 1):
        c1 = int(c / 100000)
        c2 = int(c % 100000 / 10000)
        c3 = int(c % 10000 / 1000)
        c4 = int(c % 1000 / 100)
        c5 = int(c % 100 / 10)
        c6 = int(c % 10)
        if(c1 + c2 + c3 == c4 + c5 + c6):
            sum += 1
        
    return sum
 
print("you Got " + str(Lucky_tickets()) + " Lucky tickets!")
#------------------------------------------------------------------------------ 




#------------------------------------------------------------------------------ 

def RecPrint(begin, end, skip):
    """
    
    @param begin:
    @type begin:
    @param end:
    @type end:
    @param skip:
    @type skip:
    """

    if(begin + skip >= end):
        print(begin, " ")
    else:
        print(begin, end=", ")
    if(end - skip > begin):
        RecPrint(begin + skip, end, skip)
                
RecPrint(53, 89, 10)
#------------------------------------------------------------------------------ 
