import pandas as pd 
import numpy as np 
from scipy.stats import zscore
def main():
    data={"Name":["Ravi","Sita","Kiran","Ravi","John","Anu"],"Marks":[85,90,78,85,300,88]}
    df=pd.DataFrame(data)
    print("=====ORIGINAL DATASET=====")
    print(df)
    print("\n=====DUPLICATE ROWS=====")
    print(df[df.duplicated()])
    df_no_duplicates=df.drop_duplicates()
    print("\n=====DATASET AFTER REMOVING DUPLICATES=====")
    print(df_no_duplicates)
    df_no_duplicates["Z_score"]=zscore(df_no_duplicates["Marks"])
    print("\n=====Z-SCORE=====")
    print(df_no_duplicates)
    outliers = df_no_duplicates[
    (df_no_duplicates["Z_score"] > 2) |
    (df_no_duplicates["Z_score"] < -2)]
    print("\n=====DETECTED OUTLIERS=====")
    print(outliers)
    cleaned_data=df_no_duplicates[(df_no_duplicates["Z_score"]<=2)&(df_no_duplicates["Z_score"]>=-2)]
    print("\n=====DATA AFTER REMOVING OUTLIERS=====")
    print(cleaned_data)
    print("\n=====DISTIBUTION AFTER REMOVING OUTLIERS=====")
    print(cleaned_data["Marks"].describe())
    print("\n=====DISTIBUTION AFTER REMOVING OUTLIERS=====")
    print(cleaned_data["Marks"].describe())
if __name__ == "__main__":
    main()