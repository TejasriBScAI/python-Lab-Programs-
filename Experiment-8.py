
import pandas as pd
def main():
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Arun', 'Bala', 'Charan', 'David'],
        'Marks': [85, 90, 78, 88]
    })
    df2 = pd.DataFrame({
        'ID': [3, 4, 6, 7],
        'Department': ['CSE', 'ECE', 'EEE', 'MECH'],
        'City': ['Hyderabad', 'Chennai', 'Delhi', 'Mumbai']
    })
    df3 = pd.DataFrame({
        'ID': [7, 8],
        'Name': ['Eswar', 'Farhan'],
        'Marks': [92, 81]
    })
    print("DataFrame 1")
    print(df1)
    print("\nDataFrame 2")
    print(df2)
    print("\nDataFrame 3")
    print(df3)
    inner_merge = pd.merge(df1, df2, on='ID', how='inner')
    print("\nInner Merge")
    print(inner_merge)
    right_merge = pd.merge(df1, df2, on='ID', how='right')
    print("\nRight Merge")
    print(right_merge)
    outer_merge = pd.merge(df1, df2, on='ID', how='outer')
    print("\nOuter Merge")
    print(outer_merge)
    concat_rows = pd.concat([df1, df3], ignore_index=True)
    print("\nRow-wise Concatenation")
    print(concat_rows)
    concat_columns = pd.concat([df1, df2], axis=1)
    print("\nColumn-wise Concatenation")
    print(concat_columns)
    print("\nOuter Merge with Missing Values")
    print(outer_merge)
    filled_data = outer_merge.fillna("Not Available")
    print("\nAfter Handling Missing Values")
    print(filled_data)
if __name__ == "__main__":
    main()
