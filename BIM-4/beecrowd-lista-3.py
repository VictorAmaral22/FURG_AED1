# Exrc 1

'''
def MDC (a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

trials = int(input(""))

for trial in range(trials):
    figures = input().strip().split(" ")

    print(MDC(
        int(figures[0]),
        int(figures[1])
    ))
'''

# Exrc 2

'''
fibos = [-1 for _ in range(40)]
fiboCalls = [-1 for _ in range(40)]

fibos[0], fibos[1] = [0, 1]
fiboCalls[0], fiboCalls[1] = [1, 1]

def fibo (num):
    if fibos[num] == -1:
        result1, num_calls1 = fibo(num - 1)
        result2, num_calls2 = fibo(num - 2)
        fibos[num] = result1 + result2
        fiboCalls[num] = num_calls1 + num_calls2 + 1

        return [fibos[num], fiboCalls[num]]
    else:
        return [fibos[num], fiboCalls[num]]

val = int(input(""))
result, calls = fibo(val)
print(f"fib({val}) = {calls-1} calls = {result}")
'''

# Exrc 3

'''
cases = int(input())

for case in range(1, cases + 1):
    people, salt = [int(x) for x in input().strip().split(' ')]

    left = 0
    for p in range(1, people + 1):
        left = (left + salt) % p

    print(f"Case {case}: {left + 1}")
'''

