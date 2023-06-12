import datetime

from asset_data import AssetData
from zscore import Zscore
from signal import Signal
from position import Position
from returns import Return_Calculator
from plot import View_Plot

tickers_list = ["KO", "PEP"]
start_date = (datetime.datetime.today() - datetime.timedelta(days=5*365)).strftime("%Y-%m-%d")
end_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
field_name = "Adj Close"
rolling_window = 30

assets = AssetData(tickers_list)
assets_df = assets.get_data(start_date=start_date, end_date=end_date, field_name=field_name)

asset1 = assets_df[tickers_list[0]]
asset2 = assets_df[tickers_list[1]]

zscore1 = Zscore(asset1, window=rolling_window).calculate() 
zscore2 = Zscore(asset2, window=rolling_window).calculate()

long_signal, short_signal = Signal(zscore1, zscore2, rolling_window).calculate()

asset1_position, asset2_position = Position(long_signal, short_signal).calculate()

asset1_returns, asset2_returns, portfolio_returns = Return_Calculator(asset1, asset1_position, asset2, asset2_position).calculate()

View_Plot(tickers_list, asset1_returns, asset2_returns, portfolio_returns, \
          "Long Short Pair Returns", "Total Returns", xrotation=45).plot_graph()
