#https://leetcode.com/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while True:
            if tickets[k] == 0:
                break
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] > 0:
                    tickets[i] -= 1
                    count+=1
        return count