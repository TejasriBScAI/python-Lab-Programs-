import pandas as pd 
def main():
    data={"Experiment-1":["Ravi","Sita","Kiran","Anu","John"],
"Marks":[85,90,78,92,88],
"age":[20,21,19,22,20]}
    df=pd.DataFrame(data)
    df.to_csv("Experiment.csv",index=False)
    df.to_excel("Experiment.xlsx",index=False)
    df.to_josn("Experiment.joson",orient="records")
    csv_data=pd.read_csv("Experiment.csv")
    excel_data=pd.read_json("Experiment.json")
    print("=====CSV DATA=====")
    print(csv_data)
    print("\n=====head()=====")
    print(csv_data.head())
    print("\n=====info=====")
    print(csv_data.info())
    print("\n=====describe()=====")
    print(csv-data.describe())
    print("\n=====shape=====")
    print(csv_data.shape)
if __name__ == "__main__":
    main()