import pandas as pd
# Sample DataFrame
data = {
    'Name': ['Ali', 'Ahmed', None, 'Sara', 'Ali'],
    'Age': [22, None, 25, 30, 22],
    'City': ['Lahore', 'Karachi', 'Islamabad', None, 'Lahore']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
# 3. Fill missing values
print("\nDataFrame after fillna():")
print(df.fillna("No Value"))
