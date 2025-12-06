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
# Rename columns
print("\nRenamed Columns:")
df_renamed = df.rename(columns={'Name': 'FullName', 'City': 'Location'})
print(df_renamed)
