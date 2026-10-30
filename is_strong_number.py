#Check if sum of factorials of digits equals original number (eg: 145 = 1! + 4! + 5!)

def factorials_of_digits(num):
    fact=1
    while num>0:
        fact*=num
        num-=1
    return fact

def sum_of_factorials(num):
    sum=0
    while num>0:
        sum+=factorials_of_digits(num%10)
        num//=10
    return sum

def is_strong_number(num):
    if num==sum_of_factorials(num):
        print("is strong number")
    else:
        print("not strong number")

is_strong_number(145)