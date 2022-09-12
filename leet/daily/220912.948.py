# bag of tokens
from collections import deque
from types import List

class Solution:
    def bagOfTokensScore(self, tkns: List[int], power: int) -> int:
        tokens = deque(sorted(tkns))
        score = 0
        ans = 0
        while tokens and (score>0 or power>=tokens[0]):
            if power>=tokens[0]:
                use_power = tokens.popleft()
                power -= use_power
                score += 1
                ans = score
            elif score > 0:
                get_power = tokens.pop()
                power += get_power
                score -= 1
        return ans
            