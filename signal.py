class Signal:

    def __init__(self, zscore1, zscore2, rolling_window):
        self.zscore1 = zscore1
        self.zscore2 = zscore2
        self.rolling_window = rolling_window

    def calculate(self):

        spread = self.zscore1 - self.zscore2
        spread_mean = spread.rolling(window=self.rolling_window).mean()
        spread_std = spread.rolling(window=self.rolling_window).std()

        upper_bound = spread_mean + 2 * spread_std
        lower_bound = spread_mean - 2 * spread_std

        long_signal = (spread < lower_bound).astype(int)
        short_signal = (spread > upper_bound).astype(int)

        return long_signal, short_signal