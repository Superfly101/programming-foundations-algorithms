def gcd(x, y): 

    while(y != 0):
        t = x
        x = y

        y = t % y

    return x

print(gcd(20, 8)) # should be 4
print(gcd(60, 96)) # should be 12
