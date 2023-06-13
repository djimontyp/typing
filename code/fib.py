import timeit


setup_code = """
def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x

def fibonacci_typed(n: int) -> int:
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x
"""

non_typed_code = "fibonacci(10000)"

typed_code = "fibonacci_typed(10000)"

REPEAT = 100000

non_typed_time = timeit.timeit(non_typed_code, setup=setup_code, number=REPEAT)

typed_time = timeit.timeit(typed_code, setup=setup_code, number=REPEAT)


if __name__ == "__main__":
    print(f"{non_typed_time=}", f"{typed_time=}", sep="\n")


#  non_typed_time = 82.49694463999913
#  typed_time     = 80.24413510100567
