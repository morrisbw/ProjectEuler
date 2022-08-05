#The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
z = 100
x = 1
sum = 0
y = 1
sum2 = 0
while x < z +1:
    sum = sum + (x * x)
    x = x + 1
sumofsquares = sum
#print(sumofsquares)
while y < z+1:
    sum2 = sum2 + y
    y = y + 1
squareofsums = sum2 * sum2
#print(squareofsums)
theanswer = squareofsums - sumofsquares
print(theanswer)
