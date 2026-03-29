# Program made to get a list of prime numbers until a maximum defined by user

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_list(max):
    prime_numbers = []
    for num in range(2, max + 1):
        if isprime(num):
            prime_numbers.append(num)
    return prime_numbers

max = int(input("Please enter the maximum number to complete the list: "))

if max < 2:
    print("The maximum value must be at least 2.")
else:
    prime_numbers = prime_numbers_list(max)

    print("\nList of prime numbers until", max, ":\n\n", prime_numbers)

    number_of_prime_numbers   = len(prime_numbers)

    if 1 <= number_of_prime_numbers <= 10:
        print("\n --> There is", number_of_prime_numbers, "prime numbers in this list !!")
    else:
        print("\n --> There are", number_of_prime_numbers, "prime numbers in this list !!")

    


