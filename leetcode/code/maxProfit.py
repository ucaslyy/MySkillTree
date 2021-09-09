from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices:
        :return:
        """
        max_profit = 0
        peak_value = valley_value = prices[0]
        for price in prices:
            if peak_value < price:
                peak_value = price
                max_profit = max(max_profit, peak_value-valley_value)

            if valley_value > price:
                valley_value = peak_value = price

        return max_profit
