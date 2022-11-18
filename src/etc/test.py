import random
import time
import sys

sys.setrecursionlimit(10**7)


def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        j = i
        while j > low and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def dual_pivot_sort(a, low=0, high=None, N=17):
    if high is None:
        high = len(a) - 1

    if low < high:
        if high - low + 1 < N:
            # Size of the subarray is less than the threshold, insertion sort
            insertion_sort(a, low, high)
            return
        # Size of the subarray is greater than the threshold, quicksort
        pivot_index = partition(a, low, high)
        dual_pivot_sort(a, low, pivot_index - 1)
        dual_pivot_sort(a, pivot_index + 1, high)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot, tail = array[0], array[1:]

    lp = [x for x in tail if x <= pivot]
    rp = [x for x in tail if x > pivot]

    return quick_sort(lp) + [pivot] + quick_sort(rp)


if __name__ == '__main__':
    random.seed(1995)
    K = 1000
    length = [17, 33, 65, 129, 257, 513]
    size = [10*K, 100*K, 200*K, 400*K, 800*K, 1600*K, 3200*K, 6400*K]

    d_times = []
    q_times = []
    for s in size:
        for l in length:
            numbers = [random.randint(1, 1000) for _ in range(s)]
            start = time.time()
            dual_pivot_sort(numbers, 0, len(numbers) - 1, N=l)
            d_times.append(time.time() - start)

            start = time.time()
            quick_sort(numbers)
            q_times.append(time.time() - start)
        # print('DUAL  >> size: {}, times: {}'.format(s, d_times))
        print('QUICK >> size: {}, times: {}'.format(s, q_times))
        # d_times.clear()
        q_times.clear()