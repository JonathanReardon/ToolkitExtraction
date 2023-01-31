from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
parentittle = get_metadata("ParentTitle")
parentittle_df = pd.DataFrame(parentittle)
parentittle_df.columns = ["ParentTitle"]
parentittle_df.fillna("NA", inplace=True)

# save to disk
#parentittle_df.to_csv("parentittle.csv", index=False)

""" print(parentittle_df) """
