twenty = 20
therange = 20
divisible = 0
thenumber = 40




#while divisible < 1:
    #if number % max == 0:
        #print("divisible by max", number)
        #divisible = 1
    #number = number + 1

def divisibility(anumber, divisor):
    divis = 1    
    while divis == 1:
        if anumber % divisor == 0:
            #print("yes")
            divis = 0
            return(divis)
        else:
            return(divis)
    
while therange > 2:
    a = divisibility(thenumber, therange)
    if a == 0:
        #print(a)
        #print(therange)
        #print(thenumber) 
        therange = therange -1
    else:
        #print("HERE")
        thenumber = thenumber + 1
        therange = twenty
        #print(thenumber)
print(thenumber)    
  


     