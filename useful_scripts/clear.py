import sys
import pandas as pd

filePath = str(sys.argv[1])

df = pd.read_csv(filePath)
for i in range(len(df)):
    df.loc[i, 'TIME'] = "non"
df.to_csv(filePath, index=False)
print(sys.argv[1]+"cleared")

