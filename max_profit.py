# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitFromIndex(prices, 0)

    def maxProfitFromIndex(self, prices: List[int], startIndex: int) -> int:
        maxProfitFromAllRoots = 0

        for treeRootIndex in range(startIndex, len(prices)):
            rootPrice = prices[treeRootIndex]
            rootTreeProfit = 0

            for nextNodeIndex in range(treeRootIndex + 1, len(prices)):
                nextPrice = prices[nextNodeIndex]
                nextProfit = nextPrice - rootPrice

                # this is the single line that respects when we would be doing a "transaction"
                if nextProfit > 0:

                    # this line determines that this particular transaction path is more valuable
                    # than all the other potential transaction paths we could be doing
                    thisTreeProfit = (
                        self.maxProfitFromIndex(prices, nextNodeIndex) + nextProfit
                    )

                    # assign the tree with this particular root to our top level profit tracker
                    # if its higher than our current value
                    if thisTreeProfit > rootTreeProfit:
                        rootTreeProfit = thisTreeProfit

            # assign this root to the top level profit tracker
            # this is similar to the top level profit tracker above, but it works one level higher
            # (eg. across the whole tree, rather than across a single root)
            if rootTreeProfit > maxProfitFromAllRoots:
                maxProfitFromAllRoots = rootTreeProfit

        return maxProfitFromAllRoots