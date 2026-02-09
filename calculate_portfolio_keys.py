import numpy as np




def portfolio_sigma(weights, covariance_matrix):
    """Calculate the portfolio sigma based on the weights and covariance matrix"""
    cov_matrix = covariance_matrix["cov_matrix"]

    # Ensure consistent ordering
    assets = list(weights.keys())
    w = np.array([weights[a] for a in assets])

    # Extract matching covariance sub-matrix
    Sigma = cov_matrix.loc[assets, assets].values

    # Portfolio variance
    variance = w.T @ Sigma @ w

    sigma = np.sqrt(variance)

    sigma_yearly = sigma * np.sqrt(12)

    return sigma_yearly


def calculate_portfolio_return(weights, expected_returns):
    """Calculate the portfolio returns based on the weights and the expected returns from each asset"""

    assets = list(weights.keys())
    w = np.array([weights[a] for a in assets])
    r = np.array([expected_returns[a] for a in assets])

    portfolio_return = np.dot(w,r)

    return portfolio_return


def calculate_sharpe_ratio(sigma_yearly, portfolio_return, risk_free_rate):
   """Calculate the Sharpe Ratio based on the sigma, return of the portfolio and the risk free rate"""
   sharpe_ratio = (portfolio_return-risk_free_rate) / sigma_yearly
   
   return sharpe_ratio