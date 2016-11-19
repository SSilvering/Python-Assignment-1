#===============================================================================#
#---------------------------Python Assignment 1---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#

# Question -1-
def Xnor(x, y):    
    """
    This function gets two boolean expression and returns the Xnor conclusion.
    
    @param x: Boolean expression.
    @type x:  Boolean expression.
    @param y: Boolean expression.
    @type y:  Boolean expression.
    """
    if(x == True and y == True or x == False and y == False):
        return True
    else:
        return False
    return False

print(Xnor(9 > 5, 5 < 6))              # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -2-
def Learn(age):    
    """
    This function identifies where the person studied according to age and returns the name of the place.
    
    @param age: The age of the person.
    @type age:  float.
    """
    if age >= 4 and age <= 5:
        return "Kindergarten"
    elif age >= 6 and age <= 14:
        return "Grade_School"
    elif age >= 15 and age <= 18:
        return "High_School"
    elif age >= 19 and age <= 21:
        return "Army"
    elif age >= 22 and age <= 25:
        return "SCE"
    else:
        return "None"

print(Learn(4))                        # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -3-
def IsDivBy(numerator, denominator):    
    """
    This function gets numerator and denominator. The function returns true if the result of 
    the division is without a remainder, and false if the result of the division with a remainder.
    
    @param numerator:   A number.
    @type numerator:    float.
    @param denominator: A number.
    @type denominator:  float.
    """
    
    if(denominator == 0):
        return False
    if(numerator % denominator == 0):
        return True
    else:
        return False  
    
    return False  
    
print(IsDivBy(36, 0))                  # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -4-
def Calc_pi(Iter):
    """
    This function gets the number of elements that exist in the series 
    and evaluates the value of pi according to Leibniz.
    
    @param Iter: Number of elements in series.
    @type Iter:  Integers. 
    """
    sign, pii = 1, 0.0                 # initialize parameters.
    
    for n in range(Iter):
        pii += 4 / (2 * n + 1) * sign  # evaluate specific argument in the column.
        sign *= -1                     # change sign for the next iteration.
    
    return pii

print(Calc_pi(623))                    # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -5-
def Lucky_tickets():
    """
    This function passes on all six-digit number and counts 
    the numbers that sum total of the first three digits equals
    the sum of the last three digits of the number. 
    Finally, returns the amount of numbers that maintain this condition.    
    """
    
    count = 0
    
    for val in range(100000, 1000000):
        index, partA, partB , temp = 0, 0, 0, val
        
        while temp > 0:
            if index < 3:   # Indicates about last three digits of the number.
                partA += int(temp % 10)                
                temp //= 10 # Takes only the integer part of the multiplication function.
                index += 1
            else:           # The rest of digits of that number.
                partB += int(temp % 10)
                temp //= 10 # Takes only the integer part of the multiplication function.                       
        
        if partA == partB:
            count += 1
                    
    return count

print("You've got", Lucky_tickets(), "lucky tickets!")  # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -6-
def FIer (n):
    """
    This iterated function returns the same number if it is lower or equal to 3.
    
    @param n: All the numbers that satisfy n <= 3.
    @type n: Integers.
    """
    
    if n <= 3:
        return n
    
def FRec(n):
    """
    This function calculates the sum of the column under the following conditions:    
                F(n) = n                          if n <= 3
                F(n) = F(n-1) + 2F(n-2) + 3F(n-3) if n >  3

    @param n: All the numbers that satisfy n > 3.
    @type n: Integers.
    """
    
    if n <= 3:
        return FIer(n)
    else:
        return FRec(n - 1) + 2 * FRec(n - 2) + 3 * FRec(n - 3)
    
print(FRec(5))                         # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -7-
def RecPrint(begin, end, skip):
    """
    This function gets a range of numbers, and prints them at equal intervals sets by the variable "skip".
    
    @param begin: First number of the range.
    @type begin:  Integers.
    @param end:   Last number of the range.
    @type end:    Integers.
    @param skip:  In which jump size need to be done between prints.
    @type skip:   Integers.
    """

    if begin > end:                     # Stop Condition.
        return
    if begin + skip > end:              # Prints the last number without commas and create new line.
        print(begin)
    else:
        print(begin, end=", ")          # Prints the numbers according to the skips condition.             
    
    RecPrint(begin + skip, end, skip)
                
RecPrint(-53, 107, 10)                  # Executable Line for testing
#------------------------------------------------------------------------------
# Question -8-
def Creator(num):
    """
    This function gets an integer and returns a number 
    that was built from the even numbers of the original number.
    
    @param num: Natural number, positive or negative.
    @type num: Integer.
    """

    if num < 0:                                     # Negative number check.
        return -Creator(-num)
    elif num == 0:                                  # Stop condition.
        return 0
    elif num % 2 != 0:
        return Creator(num // 10)
    else:
        return 10 * Creator(num // 10) + num % 10   # Building new number.

print(Creator(-14187))                              # Executable Line for testing
#------------------------------------------------------------------------------ 
# Question -9-
def PrintReverse(number):
    """
    This function gets a number, and prints its digits in reverse order with spaces.
    
    @param number: An integer number.
    @type number:  Integers.
    """
    
    if(number < 10):
        print("%d" % (number))
    else:
        print("%d" % (number % 10), end=" ")
        PrintReverse(int(number // 10))     # operator "//" takes only the rational  
                                            # part of the distribution function.      

PrintReverse(1245678901987654321012345678)  # Executable Line for testing
#------------------------------------------------------------------------------