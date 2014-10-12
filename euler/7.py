import util

primeCounter=0
i=0

while(primeCounter<10001):
        i+=1
        if(util.is_prime(i)):
            primeCounter+=1    
    
print primeCounter
print i