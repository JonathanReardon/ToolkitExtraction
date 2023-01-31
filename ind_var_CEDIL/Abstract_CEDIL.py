from Main import load_json, get_metadata
import pandas as pd

load_json()

# get abstract data
abstract = get_metadata("Abstract")
abstract_df = pd.DataFrame(abstract)
abstract_df.columns = ["abstract"]
abstract_df.fillna("NA", inplace=True)

abstract_df.replace('\r', ' ', regex=True, inplace=True)
abstract_df.replace('\n', ' ', regex=True, inplace=True)
abstract_df.replace(':', ' ',  regex=True, inplace=True)
abstract_df.replace(';', ' ',  regex=True, inplace=True)

# save to disk
abstract_df.to_csv("abstract.csv", index=False)

print(abstract_df)
