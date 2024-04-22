import functools
import random
import time


def function_timer(func):
    """Print runtime of the function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f'Elapsed time: {round(elapsed_time/60,6)} minutes for {func.__name__!r}')
        return value

    return wrapper


def function_debugger(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})`')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} Returned: {value!r}')
        return value

    return wrapper


def do_random_work_and_calculate(animal):
    print('Doing some random work...')
    time.sleep(random.random())
    for i in range(random.randint(1, 10)):
        print(i, end=' ')
    print(f'{animal}s!')
    time.sleep(random.random() / 10)
    print('Done with the random work!')


print('Running without decorators:')
do_random_work_and_calculate('unicorn')

print('\nRunning with timer decorator:')
timed = function_timer(do_random_work_and_calculate)
timed('owl')

print('\nRunning with debugger decorator:')
debugged = function_debugger(do_random_work_and_calculate)
debugged('tiger')

print('\nRunning with both decorators:')
timed_and_debugged = function_debugger(function_timer(do_random_work_and_calculate))
timed_and_debugged('jaguar')
