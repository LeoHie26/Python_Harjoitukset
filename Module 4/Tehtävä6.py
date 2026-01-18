import random

N = int(input("Kuinka monta satunnaispistettä generoidaan? "))

n, i = 0, 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        n += 1

    i += 1

pi_approx = 4 * n / N

print(f"Approximation of pi: {pi_approx}")

