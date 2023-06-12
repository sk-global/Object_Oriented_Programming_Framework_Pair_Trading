import datetime
import yfinance as yf

class AssetData:

    def __init__(self, tickers_list):
        self.tickers_list = tickers_list

    def get_data(self, start_date, end_date, field_name):
        assets_df = yf.download(self.tickers_list, start = start_date, end=end_date)[field_name]
        return assets_df

if __name__ == "__main__":
    
    tickers_list = ["KO", "PEP"]
    start_date = (datetime.datetime.today() - datetime.timedelta(days=5*365)).strftime("%Y-%m-%d")
    end_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    field_name = "Adj Close"

    assets = AssetData(tickers_list)
    assets_df = assets.get_data(start_date, end_date, field_name)
    assets_df.to_csv("pairs_KO_PEP.csv")

