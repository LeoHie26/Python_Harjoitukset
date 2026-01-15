import random

lock_3_digit = "".join(str(random.randint(0, 9)) for i in range(3))

lock_4_digit = "".join(str(random.randint(1, 6)) for i in range(4))

print("3-digit code:", lock_3_digit)
print("4-digit code:", lock_4_digit)
