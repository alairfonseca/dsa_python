class Solution:
    def knightProbability(self, n, k, row, column):
        if k == 0:
            return 1
        if n < 2:
            return 0
        
        steps = 0
        possibilities = self.possibles(n, row, column)
        chance = 1
    
        while steps < k:
            for possibility in possibilities:
                a = self.possibles(n, possibility[0], possibility[1])
                if not steps >= k:
                    chance *= (len(a) / 8)
                    steps += 1

        return chance

    def possibles(self, n, row, column):
        result = []
        n -= 1
        moves = [(-2, -1), (-1, -2), (+1, - 2), (+2, -1), (+2, +1), (+1, +2), (-1, +2), (-2, +1)]

        for move in moves:
            if not (row + move[0] > n or row + move[0] < 0) and not (column + move[1] > n or column + move[1] < 0):
                result.append((row + move[0], column + move[1]))

        return result
    
a = Solution()

print("---------", a.knightProbability(3, 2, 0, 0))
print("---------", a.knightProbability(3, 1, 0, 0))
print("---------", a.knightProbability(3, 3, 0, 0))
