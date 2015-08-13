"""Quick Sort"""

def q_sort(array):
    """Return sorted array."""
    if not array:
        return None
    if len(array) == 1 or max(array) == min(array):
        return array
    pivot = array[len(array) // 2]
    print pivot
    left = list()
    right = list()
    for elem in array:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    print left
    print right
    return q_sort(left) + q_sort(right)

def main():
    """Entry point for the program."""
    # None
    print q_sort([])
    # [1]
    print q_sort([1])
    # [1,1,1]
    print q_sort([1,1,1])
    # [2, 5, 7, 10]
    print q_sort([10,5,7,2])

if __name__ == '__main__':
    main()
