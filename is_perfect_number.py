# Return true if sum of proper divisors of n (excluding n itself) equals n

def divisors_sum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

def is_perfect_number(num):
    if divisors_sum(num)==num:
        print("num is perfect ")
    else:
        print("num is not perfect")

num=int(input("Enter a number:\n"))
is_perfect_number(num)