from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
pages = get_metadata("Pages")
pages_df = pd.DataFrame(pages)
pages_df.columns = ["Pages"]
pages_df.fillna("NA", inplace=True)

# save to disk
#pages_df.to_csv("pages.csv", index=False)
