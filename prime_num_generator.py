def primes(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Пример использования
prime_generator = primes(129)
for prime in prime_generator:
    print(prime)
