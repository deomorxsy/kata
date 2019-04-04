def positive_sum(arr):
    # Retorne a soma dos elementos para cada elemento em 'arr', somente se i for >= a 0.
    return sum(i for i in arr if i >= 0)