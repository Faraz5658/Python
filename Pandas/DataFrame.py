import pandas as pd
data={
    "Name":["Alice", "Bob", "Charlie"],
    "Age":[25, 30, 35],
    "City":["New York", "Los Angeles", "Chicago"],
    "salary":[70000, 80000, 90000]
}
HELLO = pd.DataFrame(data)
print(HELLO)
