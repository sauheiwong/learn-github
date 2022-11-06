from prime_class import *

for i in range(2,10**7):
    if last_number_check(i):
        print(f'{i} is prime number.')
        
print('finish')