class Solution:   
    def concatenatedBinary(self, n: int) -> int:
        binary, MOD = [], 1000000007
        for i in range(1,n+1):
            positive_binary = '{0:b}'.format(i)
            binary.append(positive_binary)
        x = ''.join(binary)
        return int(x,2) % MOD