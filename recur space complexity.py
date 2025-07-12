def sum(n):
    return n*(n+1)/2 #space complexity is 1

def arraysum(a):
    sum=0
    for i in (a):
        sum+=i
    return sum
a=[1,2,3,4]
arraysum(a) #space complexity depends on the array size, bigger array size so more iterations and the opposite is true