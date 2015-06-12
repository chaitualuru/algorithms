"""MinCoins"""

def get_min(req_sum, coins):
    """Get minimun required number of coins."""
    if req_sum == 0 or not coins:
        return None
    sums = [float("inf")] * (req_sum + 1)
    sums[0] = 0
    for coin in coins:
        for i in range(req_sum + 1):
            if i + coin < req_sum + 1:
                if sums[i] + 1 < sums[i + coin]:
                    sums[i + coin] = sums[i] + 1
    if sums[req_sum] != float("inf"):
        return sums[req_sum]
    else:
        return None

def get_min_2(req_sum, coins):
    """Get minimum required number of coins."""
    if req_sum == 0 or not coins:
        return None
    sums = [float("inf")] * (req_sum + 1)
    sums[0] = 0
    for i in range(req_sum + 1):
        for coin in coins:
            if coin <= i and sums[i - coin] + 1 < sums[i]:
                sums[i] = sums[i - coin] + 1
    if sums[req_sum] != float("inf"):
        return sums[req_sum]
    else:
        return None

def main():
    """Entry point for the program."""

    # [1, [2]] -> None
    print get_min_2(1, [2])

    # [0, [1]] -> None
    print get_min_2(0, [1])

    # [10, []] -> None
    print get_min_2(10, [])

    # [11, [2, 3, 5]] -> 3
    print get_min_2(11, [2, 3, 5])

if __name__ == '__main__':
    main()
