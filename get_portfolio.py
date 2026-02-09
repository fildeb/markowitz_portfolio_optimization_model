



def selection(df):
    """Get the stocks from the portfolio"""
    portfolio_edited = df.drop(columns=["Date", "Market", "RF"])
    portfolio = portfolio_edited.columns

    stock_selection = len(portfolio)

    
    return portfolio, stock_selection


def portfolio_weights(portfolio, portfolio_n):
    weights = {}

    equal_weigts = 1 / portfolio_n
    for stock in portfolio:
        weights[f"{stock}"] = equal_weigts

    return weights