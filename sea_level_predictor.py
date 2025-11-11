import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, alpha=0.5, color='green')

    # Create first line of best fit
    lin = linregress(x, y)
    
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = lin.slope * x_pred + lin.intercept
    plt.plot(x_pred, y_pred, "blue")

    # Create second line of best fit
    second_df = df.loc[df['Year'] >= 2000]
    x2 = second_df["Year"] 
    y2 = second_df["CSIRO Adjusted Sea Level"]
    lin2 = linregress(x2, y2)
    
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = lin2.slope * x_pred2 + lin2.intercept
    plt.plot(x_pred2, y_pred2, "red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
