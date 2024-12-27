def primes(n):
    """
    return all prime numbers less than or equal to n.

    Args:
        n (int): The upper limit to check for prime numbers.
    """
    if n < 2:
        print("No prime numbers within this range.")
        return

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for number in range(2, n + 1):
        if is_prime(number):
            yield number

for i in primes(100):
    print(i)