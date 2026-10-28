# Extract digit iteratively with n%10 and compute their sum

def sum_digits(n):
    sum=0
    while(n>0):
        last_digit=n%10
        sum=sum+last_digit
        n=n//10
    print(sum)

sum_digits(1234)
