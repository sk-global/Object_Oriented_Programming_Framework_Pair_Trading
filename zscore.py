
class Zscore:

    def __init__(self, asset, window=30):
        self.asset = asset
        self.window = window

    def calculate(self):

        asset_mean = self.asset.rolling(window=self.window).mean()
        asset_std = self.asset.rolling(window=self.window).std()
       
        asset_zscore = (self.asset - asset_mean) / asset_std
        
        return asset_zscore
    