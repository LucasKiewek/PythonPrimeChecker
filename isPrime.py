# Lucas Kiewek
# Oct 18, 2017
# Primality Test

# Input a number and it will tell you wether it is prime or not.




import math
from time import *


def is_prime(n, isPrime):#primality test function
    s=n%6 # setting s to the remainder of your number divided by six
    print "remainder: ", s


    if (s==1) or (s==5):# checks wether your number is one less or one more than a multiple of six (helpful for ruling out composite numbers)
        print 'running...' # for visual effect
        if isPrime:
            for i in xrange(3, int(math.sqrt(n)) + 1, 2): #checking if your nuber has any factors from three to the sqrt of your number +1
                if n % i == 0:
                    isPrime = False
    else:
        isPrime = False


    
    if n == 1 or n==0: # checks for oddities such as 1 or 0
        print "that's a weird number"
        
    elif isPrime or n == 2 or n==3:#if your nuber is two or three or fits rules above then it is prime
        print 'prime'
        
    else:
        print 'not prime'
 


def main():
        con = True
        isPrime = True #innocent until proven guilty
        while con:
                n = raw_input("your number or done: ") #input intager for primality testing or else kill loop
                    
                    
                if n.isdigit(): #checks if number can be an intager
                    n = int(n) #turns into an intager
                    
                    time1 = clock() #start time

                    is_prime(n, isPrime) #primality test
                    
                    finalTime = clock() - time1 #end timer
                    print "Elapsed time:  ", finalTime," seconds" #shows you time

                else:
                    con = False
                
        print "...all finished!!!"	

main()







