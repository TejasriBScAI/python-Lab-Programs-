
import pandas as pd
def main():
    data = {
        'Department': ['CSE', 'CSE', 'ECE', 'ECE', 'EEE', 'EEE'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Marks': [85, 90, 78, 88, 70, 95],
        'Salary': [50000, 52000, 48000, 51000, 45000, 55000]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame")
    print(df)
    print("\nAverage Marks Department-wise")
    group_marks = df.groupby('Department')['Marks'].mean()
    print(group_marks)
    print("\nAggregate Statistics for Salary")
    aggregate_stats = df.groupby('Department')['Salary'].agg(
        ['sum', 'mean', 'max', 'min']
    )
    print(aggregate_stats)
    print("\nAverage Marks based on Department and Gender")
    multi_group = df.groupby(['Department', 'Gender'])['Marks'].mean()
    print(multi_group)
    print("\nPivot Table for Average Marks")
    pivot_table = pd.pivot_table(
        df,
        values='Marks',
        index='Department',
        columns='Gender',
        aggfunc='mean'    )
    print(pivot_table)
    print("\nPivot Table for Salary Statistics")
    pivot_salary = pd.pivot_table(
        df,
        values='Salary',
        index='Department',
        columns='Gender',
        aggfunc=['mean', 'sum']
    )
    print(pivot_salary)
if __name__ == "__main__":
    main()
