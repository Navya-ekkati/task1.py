#sum of non-prime digits
start,end = 1, 5
sum_non_primes = 0
for num in range(start,end + 1)
    if num < 2:
        sum_non_primes += num
    else:
        factors = []
        for i in range (1, num + 1):
            if num % i == 0:
                factors += [i]
        if len(factors) > 2:
            sum_non_primes += num
print(sum_non_primes)

# GCD AND LCM
gcd = 2
a, b = 6,12
for i in range (1,min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd
print("LCM is", lcm)
print("GCD is", gcd)      

#sum of odd digits
num = 256711
oddsum = 0
 for i in str(num):
    if int(i) % 2 != 0:
        oddsum = oddsum + int(i)
print(oddsum)

#perfect number
num = 28
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(num, "isca perfect number")
else:
    print(num,"is not a perfect number")