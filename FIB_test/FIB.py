n = 5
k = 3 

##2 months to reach maturity
def FIB(n, k):
    newborn = 0
    growing = 0
    adults = 1
#Loop that goes through the life cycle of the rabbits
    for month in range(0,n):
        adults = growing + adults
        growing = newborn
        newborn = adults * k
    print(adults)
FIB(32,5)

#Other explanations and their reasoning

#No cache, but with less variables, by Kit Burshka
def fib(n, k):
    #Requires only two objects
    a, b = 1, 1
    #Note that their range starts at two, so the rabbits have already matured
    #Thus skipping the aging step of the equation
    #This is built on the fibonnaci logic below
    #Fn = Fn-1 + Fn-2 meaning the first two generations fail to matter
    for i in range(2, n):
        a, b = b, k*a + b
    return b

fib(n,k)

#With caching aka (dynamic programming) by Valdislav
fibocache = {} #make a tup[le]
def fibo(n,k):
    if n == 2 or n == 1: #If catches the first two generations
        return 1
    if (n,k) not in fibocache: #Checks cache before calculating saving time
        fibocache[(n,k)] = fibo(n-1,k) + fibo(n-2,k) * k
    return fibocache[(n,k)]
