class Return_Calculator:

    def __init__(self, asset1, asset1_position, asset2, asset2_position):
        self.asset1 = asset1
        self.asset1_position = asset1_position
        self.asset2 = asset2
        self.asset2_position = asset2_position

    def calculate(self):

        asset1_returns = self.asset1.pct_change()
        asset2_returns = self.asset2.pct_change()

        portfolio_returns = self.asset1_position.shift(1) * asset1_returns + \
                                self.asset2_position.shift(1) * asset2_returns
        
        return asset1_returns, asset2_returns, portfolio_returns