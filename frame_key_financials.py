import math
import numpy as np

# Create an empty dict
company_financials = {}



def calcluate_avarage_return(df):
    """Calculate the avarage return and store values inside a dictionary. Taking dataframe as an argument"""
    company_avarage_return_monthly = {}
    company_avarage_return_yearly = {}

    for ticker in df.head():
        if ticker != "Date":
            company_avarage_return_monthly[f"{ticker}"] = df[f"{ticker}"].mean()
            company_avarage_return_yearly[f"{ticker}"] = company_avarage_return_monthly[f"{ticker}"] * 12
            company_financials["avarage_return_monthly"] = company_avarage_return_monthly
            company_financials["avarage_return_yearly"] = company_avarage_return_yearly


def calculate_std_dev(df):
    """Calcualte te standard diviation and store values inside a dictionary. Taking dataframe as an argument"""
    company_std_dev_monthly = {}
    company_std_dev_yearly = {}

    for ticker in df:
        if ticker != "Date":
            company_std_dev_monthly[f"{ticker}"] = df[f"{ticker}"].std()
            company_std_dev_yearly[f"{ticker}"] = company_std_dev_monthly[f"{ticker}"] * math.sqrt(12)
            company_financials["standard_diviation_monthly"] = company_std_dev_monthly
            company_financials["standard_diviation_yearly"] = company_std_dev_yearly


def calculate_var(df):
    company_var = {}

    for ticker in df:
        if ticker != "Date": 
            company_var[f"{ticker}"] = df[f"{ticker}"].var()
            company_financials["variance"] = company_var


def calculate_cov(df):
    company_cov = {}

    for ticker in df:
        if ticker != "Date":
            company_cov[f"{ticker}"] = df[f"{ticker}"].cov(df["Market"])
            company_financials["covariance"] = company_cov



def cov_matrix_sample(df):
    company_financials["cov_matrix"] = df.drop(columns=["Date", "Market", "RF"]).cov()


# Intermediary step
def aux_calc(company_financials):
    company_financials["aux_calc"] = np.matmul(company_financials["variance"], company_financials["cov_matrix"])
    print (company_financials["aux_calc"])




def produce_key_financials(df):
    """Run calcluations of key financials from the dataframe.
    
    Return includes, e.g key_financials:

    [avarage_return], 
    [standard_deviation],
    [variance],
    [covariance],
    [cov_matrix]
    """

    calcluate_avarage_return(df)
    calculate_std_dev(df)
    calculate_var(df)
    calculate_cov(df)
    cov_matrix_sample(df)
    # aux_calc(company_financials)

    return company_financials