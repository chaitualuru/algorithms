"""Longest Ascending Sequence"""

def length_asc_seq(seq):
    """Get the length of the longest ascending subsequence"""
    if not seq:
        return 0

    result = 0
    asc_seq = [1] * len(seq)

    for i in range(len(seq)):
        for j in range(i):
            if seq[j] <= seq[i]:
                asc_seq[i] = max(asc_seq[j] + 1, asc_seq[i])

        result = max(result, asc_seq[i])

    return result



def main():
    """Entry point for program."""
    # [] -> 0
    print length_asc_seq([])

    # [1] -> 1
    print length_asc_seq([1])

    # [1, 1] -> 2
    print length_asc_seq([1, 1])

    # [1, 3, 5, 7] -> 4
    print length_asc_seq([1, 3, 5, 7])

    # [-1, -5, 12, -9, 13] -> 3
    print length_asc_seq([-1, -5, 12, -9, 13])

if __name__ == "__main__":
    main()
