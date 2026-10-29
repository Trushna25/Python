#Return true if sum of proper divisors of n strictly exceeds n AND return tue if sum of proper divisors of n is strictly less than n

def sum_of_divisors(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

def is_abundant_or_defficient(num):
    if sum_of_divisors(num)>num:
        print("num is abundant")
    elif sum_of_divisors(num)<num:
        print("num is defficient")
    else:
        print("num is perfect")

num=int(input("Enter a number:\n"))
is_abundant_or_defficient(num)
