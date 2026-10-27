# sum natural numbers for 1 to n using an accumlator variable in a for loop

def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("sum of natural numbers from 1 to",n,"is",sum)

num=int(input("Enter a number:\n"))
sum_natural(num)