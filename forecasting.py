import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_sales(df):

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    monthly = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

    X = np.arange(len(monthly)).reshape(-1,1)
    y = monthly.values

    model = LinearRegression().fit(X,y)

    future = model.predict([[len(monthly)+1]])

    return future[0]
