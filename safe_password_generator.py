import random
import string

password = "".join(random.choice(string.ascii_letters) for _ in range(8))
print(password)  # something like: 'aZxPqLrT'
