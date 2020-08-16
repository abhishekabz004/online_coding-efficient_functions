# normal procedure to find the combination (nCr) value

# Returns factorial of n 
def fact:
    res = 1  
    for i in range(2, n+1): 
        res = res * i 
    return res 
    
def normal_combination(n, r):
    return int( fact(n)/ ( fact(n-r) * fact(r) ) )            # But this wont work for large values of n and r
    
    
    
 
# Simplfying the formula for nCr = n! / ( (n-r)! * r! ) would give us the below method.
# This works even for larger numbers

def nCr(n, r): 
    numerator = 1
    denominator = 1
    prod = 1
    for i in range(r):
        numerator *= (n-i)
        denominator *= (r-i)
        if i % 10 == 1:
            prod *= (numerator/denominator)
            numerator = 1
            denominator =1
    prod *= (numerator/denominator)

    return math.floor(prod)
    
    
