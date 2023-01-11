from typing import List


class Solution:

    def path_cost(self, n, start, net_costs) -> int:
        sum = 0
        for i in range(n):
            j = ((i + start) % n)
            sum += net_costs[j]
            if sum < 0:
                return -1
        return sum

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net_costs = list(map((lambda gas, cost: gas - cost), gas, cost))
        for i in range(n):
            if self.path_cost(n, i, net_costs) >= 0:
                return i
