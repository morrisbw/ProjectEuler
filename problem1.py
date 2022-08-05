#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
# a is 2-D matrix with integers
themax = 1000
thesum = 0
factor1 = 3
factor2 = 5

for i in range(themax):
    if i % factor1 == 0:
        thesum = thesum + i
        i = i + 1
    elif i % factor2 == 0:
        thesum = thesum + i
        i = i + 1
print(thesum)
   