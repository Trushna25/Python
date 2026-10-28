# Multiply all individual digits of positive integer n using iterative extraction

def product_digits(n):
    product=1
    while(n>0):
        last_digit=n%10
        product=product*last_digit
        n=n//10
    print(product)

    for i in n:
        product*=int(i)
    print(product)

n=input("Enter a number:\n")
product_digits(n)