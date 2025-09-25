import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.head(20)
    
    years = range(1880, 2051)
    # Create scatter plot
    fig = plt.figure(figsize=(8,8))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"], marker="o", edgecolors="k")
    # Create first line of best fit
    fit1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)
    plt.plot(years, fit1.slope*years + fit1.intercept, label="first fit")
    # Create second line of best fit
    fit2 = linregress(x=df[df["Year"] >= 2000]["Year"], y=df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    plt.plot(years_recent, fit2.slope*years_recent + fit2.intercept, label="second fit")
    
    
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()