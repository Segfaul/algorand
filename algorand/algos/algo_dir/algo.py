import base64
from io import BytesIO
from time import time

import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray
from typing import Callable


def interpolation_search(sequence: [int or float] or ndarray, target: int or float) -> int:

    if type(sequence) == list:
        if not sequence or sequence != sorted(sequence):
            return -1

    elif type(sequence) == ndarray:
        if not sequence.any():
            return -1
    else:
        return -1

    l, r = 0, (len(sequence) - 1)
    while (l <= r) and (sequence[l] <= target <= sequence[r]):
        index = int((target - sequence[l]) * (l - r) // (sequence[l] - sequence[r]) + l)

        if sequence[index] < target:
            l = index + 1

        elif sequence[index] > target:
            r = index - 1

        else:
            return index

    return -1


def fibonacci_search(sequence: [int or float], target: int or float) -> int:

    if type(sequence) == list:
        if not sequence or sequence != sorted(sequence):
            return -1

    elif type(sequence) == ndarray:
        if not sequence.any():
            return -1
    else:
        return -1

    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    while fib_m < len(sequence):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2
    index = -1

    while fib_m > 1:
        i = min(index + fib_m_minus_2, (len(sequence) - 1))

        if sequence[i] < target:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            index = i

        elif sequence[i] > target:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and index < (len(sequence) - 1) and sequence[index + 1] == target:
        return index + 1

    return -1


def binary_search(sequence: [int or float], target: int or float) -> int:

    if type(sequence) == list:
        if not sequence or sequence != sorted(sequence):
            return -1

    elif type(sequence) == ndarray:
        if not sequence.any():
            return -1
    else:
        return -1

    first = 0
    last = len(sequence) - 1
    index = -1

    while (first <= last) and (index == -1):
        mid = (first + last) // 2

        if sequence[mid] == target:
            index = mid
        else:
            if target < sequence[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return index


def measure_execution_time(function: Callable, *args):
    start_time = time()

    function(*args)

    end_time = time()
    execution_time = end_time - start_time

    return execution_time


def summary():
    sizes = [500_000, 2_000_000, 5_000_000, 10_000_000]
    data = []
    for size in sizes:
        # data.append(np.random.randint(low=0, high=100, size=size))
        data.append(np.unique(np.arange(size)))

    times_algorithm = {
        'interpolation_search': [],
        'fibonacci_search': [],
        'binary_search': []
    }

    for arr in data:
        arr.sort()
        print(arr)
        search_value = arr[0]
        times_algorithm['interpolation_search'].append(
            measure_execution_time(interpolation_search, arr, search_value)
        )
        times_algorithm['fibonacci_search'].append(
            measure_execution_time(fibonacci_search, arr, search_value)
        )
        times_algorithm['binary_search'].append(
            measure_execution_time(binary_search, arr, search_value)
        )

    plt.clf()

    plt.figure(figsize=(20, 12))

    plt.plot(
        sizes,
        times_algorithm['interpolation_search'],
        label='interpolation_search',
        linestyle='-',
        color='blue'
    )
    plt.plot(
        sizes,
        times_algorithm['fibonacci_search'],
        label='fibonacci_search',
        linestyle='--',
        color='green'
    )
    plt.plot(
        sizes,
        times_algorithm['binary_search'],
        label='binary_search',
        linestyle=':',
        color='red'
    )
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time')
    plt.title('Algorithm Performance')
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return image_base64
