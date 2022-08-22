import math

def primenumber(testnumber):
    if testnumber <= 1: # 1 is by definition not prime
        return False
    elif testnumber % 2 == 0: #takes care of all even numbers including 2
        return False
    elif testnumber == 3: # 3 is prime
        return True
    else:
        counter = 3
        while counter < math.sqrt(testnumber) + 1:
            if testnumber % counter == 0:
                return False
            counter = counter + 2
            #print("Counter =" + str(counter) + "\n")
        return True

tenthousandfirstprime = 0
thenumber = 10001
#thenumber = 7
testnumber = 13
totalprimes = 1 # 2 is prime, but counter will start at 3
counter = 3 # start at 3 because we know 2 is prime(we know 3 is prime to but gotta start somewhere)

while totalprimes < thenumber:    
    if primenumber(counter) == True:
        #print("Counter = " + str(counter) + " is " + str(primenumber(counter)) + "\n")
        totalprimes = totalprimes + 1
        if totalprimes == thenumber:
            print("holy buckets")
            tenthousandfirstprime = counter
    counter = counter + 2
print(totalprimes)
print("\n" + str(tenthousandfirstprime))


    