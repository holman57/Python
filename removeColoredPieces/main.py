import re
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors)) > sum(
            len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))
