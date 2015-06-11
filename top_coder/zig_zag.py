class ZigZag:
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

zz = ZigZag()
print zz.longestZigZag([1,3,1,6,10])