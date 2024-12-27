import time


def timeit(func):
    def timed_func(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"{func.__name__} took {duration} seconds")

    return timed_func


@timeit
def for_loop(iterations):
    even_numbers = []
    odd_numbers = []
    for i in range(iterations):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return (even_numbers, odd_numbers)


@timeit
def list_comp(iterations):
    even_numbers = [i for i in range(iterations) if i % 2 == 0]
    odd_numbers = [i for i in range(iterations) if i % 2 != 0]
    return (even_numbers, odd_numbers)


if __name__ == "__main__":
    iterations = 100000000
    print(f"Sorting even and odd of {iterations} numbers.")
    for_loop(iterations)
    list_comp(iterations)
