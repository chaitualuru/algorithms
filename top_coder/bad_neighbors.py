"""Bad Neighbors"""

def get_max_straight(donations):
    """Return maximum donation possible for straight line neighbors."""
    if len(donations) <= 2:
        return max(donations)

    max_don = 0
    don_so_far = donations[:]

    for i in range(len(donations)):
        for j in range(i):
            if i - j >= 2:
                if i == len(donations) - 1:
                    don_so_far[i] = max(don_so_far[i] - donations[0], \
                        donations[i] + don_so_far[j] - donations[0])
                else:
                    don_so_far[i] = max(don_so_far[i], donations[i] + don_so_far[j])
        max_don = max(max_don, don_so_far[i])

    return max_don


def main():
    """Entry point for program."""
	# 10
    print get_max_straight([10])

	# 15
    print get_max_straight([10, 15])

	# 16
    print get_max_straight([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

    # 3200
    print get_max_straight([1000, 10, 10, 1000, 1500, 1200, 10])

    # 2710
    print get_max_straight([1000, 10, 10, 1000, 1500, 10, 1200])

if __name__ == "__main__":
    main()
