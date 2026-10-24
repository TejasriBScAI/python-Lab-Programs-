import pandas as pd 
def main():
    data={'RollNo':[101,102,103,104,105],
    'Name':['Arun','Bhanu','Charan','Divya','Esha'],
    'Marks':[85,72,90,65,88],
    'Department':['CSE','ECE','CSE','EEE','ECE']}
    df=pd.DataFrame(data)
    print("Original DataFrame")
    print(df)
    print("\nSelecting Name and Marks Columns")
    print(df[['Name','Marks']])
    print("\nSelecting Row with Index 2")
    print(df.loc[2])
    print("\nSlicing Rows from Index 1 to 3")
    print(df[1:4])
    print("\nStudents with Marks Greater than 80")
    print(df[df['Marks']>80])
    print("\nCSE Students with Marks Greater than 80")
    print(df[(df['Department']=='CSE')&(df['Marks']>80)])
    print("\nAdvanced Slicing using loc")
    print(df.loc[1:3,['Name','Marks']])
    print("\nAdvanced Slicing using iloc")
    print(df.iloc[0:3, 1:4])
if __name__ == "__main__":
    main()