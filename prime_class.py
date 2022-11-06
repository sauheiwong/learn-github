def prime_check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def last_number_check(x):
    last_no = str(x)[-1]
    if x == 2 or x == 5:
        return True
    elif int(last_no) in (2,4,5,6,8,0):
        return False
    else:
        return prime_check(x)