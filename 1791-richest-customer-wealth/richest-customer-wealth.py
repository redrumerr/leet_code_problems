class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ma_wealth = -1
        for customer in range(len(accounts)):
            customer_wealth = 0
            for bank in range(len(accounts[customer])):
                customer_wealth +=  accounts[customer][bank]
            if ma_wealth < customer_wealth:
                ma_wealth = customer_wealth
        return ma_wealth
        