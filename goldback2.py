def is_prime(n):
   if (n == 1):
       return False
   limit = int (n ** 0.5) + 1
   divisor = 2
   while (divisor < limit):
       if (n % divisor == 0):
           return False
       divisor += 1
   return True

def main():
    lo = int(input("Enter the lower limit:"))
    hi = int(input("Enter the upper limit:"))

    while (lo < 4 or hi < lo or lo%2 != 0 or hi%2 != 0):
       lo = int(input("Enter the lower limit:"))
       hi = int(input("Enter the upper limit:"))

    count = lo
    while (count <= hi):
        print (count, end = " ")
        n = 2
        limit = count // 2
        while (n <= limit):
            if (is_prime(n) and is_prime(count - n)):
                print(" = " + str(n) + " + " + str(count - n), end = " ")
            n = n + 1
        count = count + 2
        print()


main()
