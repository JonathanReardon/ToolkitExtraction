from Main import get_metadata
import pandas as pd

# get eppiID data
eppiid = get_metadata("ItemId")
eppiid_df = pd.DataFrame(eppiid)
eppiid_df.columns = ["id"]
eppiid_df.fillna("NA", inplace=True)

# save to disk
eppiid_df.to_csv("eppiid.csv", index=False)
