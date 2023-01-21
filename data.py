import pandas as pd

df = pd.read_json("AequitasData.json")

print(df)

print(df['MessageType'].info())

