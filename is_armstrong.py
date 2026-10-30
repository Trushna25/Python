# count digits manually then verify if sum of each digit raised to digit count equals n

def count_of_digits(num):
    count=0
    while(num>0):
        num=num//10
        count+=1
    return count

def sum_of_digits(num):
    sum=0
    count=count_of_digits(num)
    while num>0:
        last_digit=num%10
        power= last_digit**count
        sum+=power
        num//=10
    return sum

def is_armstrong(num):
    if num==sum_of_digits(num):
        print("is armstrong")
    else:
        print("not armstrong")

num=int(input("Enter a number:\n"))
is_armstrong(num)