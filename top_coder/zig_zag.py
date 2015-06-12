import sys

class ZigZag(object):
    def longestZigZag(self, sequence):
        length = 1
        up = [1] * (len(sequence))
        down = [1] * (len(sequence))
        for i in range(len(sequence)):
            for j in range(i):
                if sequence[i] > sequence[j]:
                    up[i] = max(down[j] + 1, up[i])
                if sequence[j] > sequence[i]:
                    down[i] = max(up[j] + 1, down[i])
            length = max(length, up[i], down[i])
        return length

def main():
    zz = ZigZag()

    # [1] => 1
    print zz.longestZigZag([1])

    # [1,2] => 2
    print zz.longestZigZag([1, 2])

    # [1,5,2,7,3,2] => 5
    print zz.longestZigZag([1, 5, 2, 7, 3, 2])

    # [1,1,1] => 1
    print zz.longestZigZag([1, 1, 1])

    # [1,2,3,4,5] => 2
    print zz.longestZigZag([1, 2, 3, 4, 5])


if __name__ == '__main__':
    sys.exit(main())
