#A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
max = 999
a = max
b = a
aholder = max
ispalin = 0
largestpalin = 0
def digitizer(n, m):
    value = n * m
    digitarray = []
    palindrome = 0
    while value > max/2:
        while value > 0:
            digit = value % 10
            value = value // 10
            digitarray += [digit]   
        if digitarray[0] == digitarray[len(digitarray)-1]:
            if digitarray[1] == digitarray[len(digitarray)-2]:
                if digitarray[2] == digitarray[len(digitarray)-3]:
                    palindrome = 1
            else:
                palindrome = 0      
        else:
            palindrome = 0  
        return (n, m, palindrome)    

while b > 90:
    while a > 90:
        a,b, ispalin = digitizer(a,b)
        if ispalin == 1:
            if (a*b) > largestpalin:
                largestpalin = (a*b)
        a = a - 1
    a = aholder - 1
    b = b - 1            
print(largestpalin)