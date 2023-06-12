import matplotlib.pyplot as plt

class View_Plot:

    def __init__(self, tickers_list, asset1_returns, asset2_returns, \
                 portfolio_returns, graph_title, ylabel, xrotation) -> None:
        self.tickers_list = tickers_list
        self.asset1_returns = asset1_returns
        self.asset2_returns = asset2_returns
        self.portfolio_returns = portfolio_returns
        self.graph_title = graph_title
        self.ylabel = ylabel
        self.xrotation = xrotation

    def plot_graph(self):
        plt.plot(((1+self.asset1_returns).cumprod()-1)*100, label=self.tickers_list[0])
        plt.plot(((1+self.asset2_returns).cumprod()-1)*100, label=self.tickers_list[1])
        plt.plot(((1+self.portfolio_returns).cumprod()-1)*100, label=f"{self.tickers_list[0]}__{self.tickers_list[1]} Pair")
        plt.title(self.graph_title)
        plt.ylabel(f"{self.ylabel} (%)")
        plt.xticks(rotation = self.xrotation)
        plt.legend()
        plt.show()


