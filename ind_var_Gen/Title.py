from Main import load_json, get_metadata
import pandas as pd

load_json()

# get eppiID data
title = get_metadata("Title")
title_df = pd.DataFrame(title)
title_df.columns = ["title"]
title_df.fillna("NA", inplace=True)

# save to disk
""" title_df.to_csv("title.csv", index=False) """

""" print(title_df) """
