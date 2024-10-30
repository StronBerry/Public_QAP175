def primes(m):
    for num in range(2, m + 1):
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num

def test_primes_1():
    return list(primes(1)) == []

def test_primes_10():
    return list(primes(10)) == [2, 3, 5, 7]

def test_primes_20():
    return list(primes(20)) == [2, 3, 5, 7, 11, 13, 17, 19]

import warnings
warnings.filterwarnings('ignore')

tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

# Запуск всех тестов
run_test(test_primes_1)
run_test(test_primes_10)
run_test(test_primes_20)

print(tests_run, tests_failed)
