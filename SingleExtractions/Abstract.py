from Main import get_metadata
import pandas as pd

# get abstract data
abstract = get_metadata("Abstract")
abstract_df = pd.DataFrame(abstract)
abstract_df.columns = ["abstract"]
abstract_df.fillna("NA", inplace=True)

# save to disk
abstract_df.to_csv("abstract.csv", index=False)
