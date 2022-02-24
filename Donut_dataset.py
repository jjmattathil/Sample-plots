""" Generate donut dataset"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def sum_x1x2(df):
    return df["x2^2"]+df["x1^2"]
def main():
    df=pd.DataFrame(columns=["x1","x2","y"])
    x=np.linspace(-20,20,2000)
    noise=np.random.random(2000)
    df["x1"]=5*np.sin(x)+noise
    df["x2"]=5*np.cos(x)+noise
    df["y"]=np.ones(2000)
    df.iloc[1000:]=2*df.iloc[1000:]
    df["x1^2"]=df["x1"]**2
    df["x2^2"]=df["x2"]**2
    df["sum"]=df.apply(sum_x1x2,axis=1)
    df["x1"] = df["x1"] + np.random.normal(0, 0.1)
    plt.scatter(df["x1"],df["x2"],c=df["y"])
    plt.axis('equal')
    plt.show()
    df.to_csv("Pandas_csv",index=False,header=False)
if __name__=="__main__":
    main()
