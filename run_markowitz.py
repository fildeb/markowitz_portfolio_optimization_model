import frame_key_financials
import get_portfolio
import calculate_portfolio_keys

import pandas as pd
from pathlib import Path



BASE_DIR = Path.cwd()
STOCK_DATA = BASE_DIR / "stock_data.xlsx"
df = pd.read_excel(STOCK_DATA)



key_financials = frame_key_financials.produce_key_financials(df)
portfolio, stock_selection = get_portfolio.selection(df)

weights = get_portfolio.portfolio_weights(portfolio,
                                          stock_selection)

sigma_yearly = calculate_portfolio_keys.portfolio_sigma(weights,
                                                        key_financials)

portfolio_return = calculate_portfolio_keys.calculate_portfolio_return(weights,
                                                                       key_financials["avarage_return_yearly"])

sharpe_ratio = calculate_portfolio_keys.calculate_sharpe_ratio(sigma_yearly,
                                                               portfolio_return,
                                                               risk_free_rate=0.03)

print (f"Portfolio Expected Return: {portfolio_return}")
print (f"Portfolio Sharpe Ratio: {sharpe_ratio}")