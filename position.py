import numpy as np

class Position:

    def __init__(self, long_signal, short_signal):
        self.long_signal = long_signal
        self.short_signal = short_signal

    def calculate(self):

        asset1_position = self.long_signal - self.short_signal
        asset2_position = self.short_signal - self.long_signal

        asset1_position[asset1_position == 0] = np.NaN
        asset1_position.ffill(inplace=True)

        asset2_position[asset2_position == 0] = np.NaN
        asset2_position.ffill(inplace=True)

        asset1_position[asset1_position<0] = 0
        asset2_position[asset2_position<0] = 0

        return asset1_position, asset2_position
