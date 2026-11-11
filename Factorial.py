def fact(n):
    '''  This is the recursive function to find the factorial of a integer'''

    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact.__doc__)
print("Factorial of 5",fact(5))
print("Factorial of 7",fact(7))