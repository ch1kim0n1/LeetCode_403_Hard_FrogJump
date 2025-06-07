class Solution:
    def canCross(self, stones):
        n = len(stones)
        idx = {stones[i]: i for i in range(n)}
        dp = [0] * n
        dp[0] = 1
        get = idx.get
        last = n - 1
        for i in range(n):
            bits = dp[i]
            if bits:
                nb = (bits | (bits << 1) | (bits >> 1)) & ~1
                p = stones[i]
                while nb:
                    lsb = nb & -nb
                    nb ^= lsb
                    k = lsb.bit_length() - 1
                    j = get(p + k)
                    if j is not None:
                        if j == last:
                            return True
                        dp[j] |= 1 << k
        return False
