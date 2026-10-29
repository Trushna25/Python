# Reverse an integer mathematically: rev = rev*10 +(n%10) without string conversion

def reverse_int(n):
    rev=0
    while(n>0):
        last_digit=n%10
        rev=rev*10 + (last_digit)
        n=n//10
    print(rev)

reverse_int(123)