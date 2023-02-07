from Main import load_json, get_metadata
import pandas as pd

load_json()

# get eppiID data
shorttitle = get_metadata("Title")
shorttitle_df = pd.DataFrame(shorttitle)
shorttitle_df.columns = ["title"]
shorttitle_df.fillna("NA", inplace=True)

# save to disk
#shorttitle_df.to_csv("shorttitle.csv", index=False)
